package com.vev.tdd.data.usecases;

import com.vev.tdd.data.protocols.AdicionaNotaRepository;
import com.vev.tdd.data.protocols.EnviaNotaERP;
import com.vev.tdd.data.protocols.EnviaNotaEmail;
import com.vev.tdd.domain.models.Fatura;
import com.vev.tdd.domain.models.NotaFiscal;
import com.vev.tdd.domain.usecases.GerarNotaFiscal;

import java.math.BigDecimal;

public class GerarNotaFiscalImpl implements GerarNotaFiscal {
    private EnviaNotaEmail enviaNotaEmail;
    private EnviaNotaERP enviaNotaERP;
    private AdicionaNotaRepository adicionaNotaRepository;

    public GerarNotaFiscalImpl(EnviaNotaEmail enviaNotaEmail, EnviaNotaERP enviaNotaERP, AdicionaNotaRepository adicionaNotaRepository) {
        this.enviaNotaEmail = enviaNotaEmail;
        this.enviaNotaERP = enviaNotaERP;
        this.adicionaNotaRepository = adicionaNotaRepository;
    }

    @Override
    public NotaFiscal gerar(Fatura fatura) {
        BigDecimal valorImposto = fatura.getValor().multiply(BigDecimal.valueOf(porcentagemImposto(fatura.getTipo())));
        NotaFiscal nota = new NotaFiscal(fatura.getNome(), fatura.getValor(), valorImposto);
        this.adicionaNotaRepository.salva(nota);
        this.notifica(nota);
        return nota;
    }

    private double porcentagemImposto(String tipo) {
        return switch (tipo) {
            case "CONSULTORIA" -> 0.25;
            case "TREINAMENTO" -> 0.15;
            default -> 0.06;
        };
    }

    private void notifica(NotaFiscal nota) {
        this.enviaNotaEmail.envia(nota);
        this.enviaNotaERP.envia(nota);
    }
}
