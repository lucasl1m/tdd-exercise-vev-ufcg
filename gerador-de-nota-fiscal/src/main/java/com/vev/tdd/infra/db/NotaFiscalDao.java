package com.vev.tdd.infra.db;

import com.vev.tdd.data.protocols.AdicionaNotaRepository;
import com.vev.tdd.domain.models.NotaFiscal;

public class NotaFiscalDao implements AdicionaNotaRepository {
    @Override
    public void salva(NotaFiscal nota) {
        System.out.println("salvando no banco");
    }
}
