package com.vev.tdd.domain.usecases;

import com.vev.tdd.domain.models.Fatura;
import com.vev.tdd.domain.models.NotaFiscal;

public interface GerarNotaFiscal {
    public NotaFiscal gerar(Fatura fatura);
}
