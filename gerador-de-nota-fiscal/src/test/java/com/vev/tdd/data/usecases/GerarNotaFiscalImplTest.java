package com.vev.tdd.data.usecases;

import com.vev.tdd.data.protocols.AdicionaNotaRepository;
import com.vev.tdd.data.protocols.EnviaNotaERP;
import com.vev.tdd.data.protocols.EnviaNotaEmail;
import com.vev.tdd.domain.models.Fatura;
import com.vev.tdd.domain.models.NotaFiscal;
import com.vev.tdd.domain.usecases.GerarNotaFiscal;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.ArgumentMatchers.*;
import static org.mockito.Mockito.*;

class GerarNotaFiscalImplTest {
    private GerarNotaFiscal sut;
    private Fatura fatura;
    private EnviaNotaEmail enviaNotaEmail;
    private EnviaNotaERP enviaNotaERP;
    private AdicionaNotaRepository adicionaNotaRepository;

    @BeforeEach
    void setUp() {
        enviaNotaEmail = mock(EnviaNotaEmail.class);
        enviaNotaERP = mock(EnviaNotaERP.class);
        adicionaNotaRepository = mock(AdicionaNotaRepository.class);
        sut = new GerarNotaFiscalImpl(enviaNotaEmail, enviaNotaERP, adicionaNotaRepository);
        fatura = new Fatura("qualquer-nome", "qualquer-endereco", "qualquer-tipo", BigDecimal.valueOf(100));
    }

    @Test
    void testNomeDoCliente() {
        NotaFiscal nota = sut.gerar(fatura);
        assertEquals(fatura.getNome(), nota.getNomeCliente());
    }

    @Test
    void testValorDaNota() {
        NotaFiscal nota = sut.gerar(fatura);
        assertEquals(0, fatura.getValor().compareTo(nota.getValor()));
    }

    @Test
    void testValorDoImpostoConsultoria() {
        Fatura fatura = new Fatura("qualquer-nome", "qualquer-endereco", "CONSULTORIA", BigDecimal.valueOf(100));
        NotaFiscal nota = sut.gerar(fatura);
        BigDecimal valorEsperado = BigDecimal.valueOf(25);
        assertEquals(0, valorEsperado.compareTo(nota.getValorImposto()));
    }

    @Test
    void testValorDoImpostoTreinamento() {
        Fatura fatura = new Fatura("qualquer-nome", "qualquer-endereco", "TREINAMENTO", BigDecimal.valueOf(100));
        NotaFiscal nota = sut.gerar(fatura);
        BigDecimal valorEsperado = BigDecimal.valueOf(15);
        assertEquals(0, valorEsperado.compareTo(nota.getValorImposto()));
    }

    @Test
    void testValorDoImpostoOutro() {
        Fatura fatura = new Fatura("qualquer-nome", "qualquer-endereco", "OUTRO", BigDecimal.valueOf(100));
        NotaFiscal nota = sut.gerar(fatura);
        BigDecimal valorEsperado = BigDecimal.valueOf(6);
        assertEquals(0, valorEsperado.compareTo(nota.getValorImposto()));
    }

    @Test
    void testEmailEnviado() {
        doNothing().when(enviaNotaEmail).envia(any(NotaFiscal.class));
        NotaFiscal nota = sut.gerar(fatura);
        verify(enviaNotaEmail, times(1)).envia(nota);
    }

    @Test
    void testNotaEnviadaERP() {
        doNothing().when(enviaNotaERP).envia(any(NotaFiscal.class));
        NotaFiscal nota = sut.gerar(fatura);
        verify(enviaNotaERP, times(1)).envia(nota);
    }

    @Test
    void testNotaAdicionadaNoBanco() {
        doNothing().when(adicionaNotaRepository).salva(any(NotaFiscal.class));
        NotaFiscal nota = sut.gerar(fatura);
        verify(adicionaNotaRepository, times(1)).salva(nota);
    }
}