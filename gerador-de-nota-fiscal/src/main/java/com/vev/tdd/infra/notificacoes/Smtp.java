package com.vev.tdd.infra.notificacoes;

import com.vev.tdd.data.protocols.EnviaNotaEmail;
import com.vev.tdd.domain.models.NotaFiscal;

public class Smtp implements EnviaNotaEmail {
    @Override
    public void envia(NotaFiscal nota) {
        System.out.println("enviando por email");
    }
}
