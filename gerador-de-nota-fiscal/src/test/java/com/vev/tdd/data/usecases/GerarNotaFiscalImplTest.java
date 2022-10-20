package com.vev.tdd.data.usecases;

import com.vev.tdd.domain.models.Fatura;
import com.vev.tdd.domain.models.NotaFiscal;
import com.vev.tdd.domain.usecases.GerarNotaFiscal;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;

import static org.junit.jupiter.api.Assertions.*;

class GerarNotaFiscalImplTest {
    GerarNotaFiscal sut;
    Fatura fatura;

    @BeforeEach
    void setUp() {
        sut = new GerarNotaFiscalImpl();
        fatura = new Fatura("qualquer-nome", "qualquer-endereco", "qualquer-tipo", BigDecimal.valueOf(100));
    }

    @Test
    void testNomeDoCliente() {
        NotaFiscal nota = sut.gerar(fatura);
        assertEquals(fatura.getNome(), nota.getNomeCliente());
    }
}