package com.vev.tdd.data.usecases;

import com.vev.tdd.data.protocols.EnviaNotaEmail;
import com.vev.tdd.domain.models.Fatura;
import com.vev.tdd.domain.models.NotaFiscal;
import com.vev.tdd.domain.usecases.GerarNotaFiscal;

import java.math.BigDecimal;

public class GerarNotaFiscalImpl implements GerarNotaFiscal {
    private EnviaNotaEmail enviaNotaEmail;

    public GerarNotaFiscalImpl(EnviaNotaEmail enviaNotaEmail) {
        this.enviaNotaEmail = enviaNotaEmail;
    }

    @Override
    public NotaFiscal gerar(Fatura fatura) {
        BigDecimal valorImposto = fatura.getValor().multiply(BigDecimal.valueOf(porcentagemImposto(fatura.getTipo())));
        NotaFiscal nota = new NotaFiscal(fatura.getNome(), fatura.getValor(), valorImposto);
        this.enviaNotaEmail.envia(nota);
        return nota;
    }

    private double porcentagemImposto(String tipo) {
        return switch (tipo) {
            case "CONSULTORIA" -> 0.25;
            case "TREINAMENTO" -> 0.15;
            default -> 0.06;
        };
    }
}
