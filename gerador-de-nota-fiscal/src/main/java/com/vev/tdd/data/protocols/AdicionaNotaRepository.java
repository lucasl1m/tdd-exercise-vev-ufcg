package com.vev.tdd.data.protocols;

import com.vev.tdd.domain.models.NotaFiscal;

public interface AdicionaNotaRepository {
    public void salva(NotaFiscal nota);
}
