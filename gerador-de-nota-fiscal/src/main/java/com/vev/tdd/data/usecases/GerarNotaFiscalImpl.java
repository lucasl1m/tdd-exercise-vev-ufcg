package com.vev.tdd.data.usecases;

import com.vev.tdd.domain.models.Fatura;
import com.vev.tdd.domain.models.NotaFiscal;
import com.vev.tdd.domain.usecases.GerarNotaFiscal;

import java.math.BigDecimal;

public class GerarNotaFiscalImpl implements GerarNotaFiscal {
    @Override
    public NotaFiscal gerar(Fatura fatura) {
        NotaFiscal nota = new NotaFiscal(fatura.getNome(), fatura.getValor(), BigDecimal.valueOf(0));
        return nota;
    }
}
