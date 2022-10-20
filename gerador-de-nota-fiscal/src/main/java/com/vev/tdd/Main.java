package com.vev.tdd;

import com.vev.tdd.data.protocols.AdicionaNotaRepository;
import com.vev.tdd.data.protocols.EnviaNotaERP;
import com.vev.tdd.data.protocols.EnviaNotaEmail;
import com.vev.tdd.data.usecases.GerarNotaFiscalImpl;
import com.vev.tdd.domain.models.Fatura;
import com.vev.tdd.domain.models.NotaFiscal;
import com.vev.tdd.domain.usecases.GerarNotaFiscal;
import com.vev.tdd.infra.db.NotaFiscalDao;
import com.vev.tdd.infra.notificacoes.SAP;
import com.vev.tdd.infra.notificacoes.Smtp;

import java.math.BigDecimal;

public class Main {
    public static void main(String[] args) {
        AdicionaNotaRepository adicionaNotaRepository = new NotaFiscalDao();
        EnviaNotaEmail enviaNotaEmail = new Smtp();
        EnviaNotaERP enviaNotaERP = new SAP();

        GerarNotaFiscal gerarNotaFiscal = new GerarNotaFiscalImpl(enviaNotaEmail, enviaNotaERP, adicionaNotaRepository);

        Fatura fatura = new Fatura("Pedro Nobrega", "Rua 123", "CONSULTORIA", new BigDecimal(1000));

        NotaFiscal nota = gerarNotaFiscal.gerar(fatura);
        System.out.println(nota);
    }
}