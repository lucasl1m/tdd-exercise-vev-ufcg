package com.vev.tdd.data.protocols;

import com.vev.tdd.domain.models.NotaFiscal;

public interface EnviaNotaEmail {
    public void envia(NotaFiscal nota);
}

