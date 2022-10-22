package com.vev.tdd.infra.notificacoes;

import com.vev.tdd.data.protocols.EnviaNotaERP;
import com.vev.tdd.domain.models.NotaFiscal;

public class SAP implements EnviaNotaERP {

    @Override
    public void envia(NotaFiscal nota) {
        System.out.println("enviando pro sap");
    }
}
