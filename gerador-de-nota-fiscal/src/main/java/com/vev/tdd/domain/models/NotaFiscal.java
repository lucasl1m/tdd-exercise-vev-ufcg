package com.vev.tdd.domain.models;

import java.math.BigDecimal;
import java.util.Objects;

public class NotaFiscal {
    private String nomeCliente;
    private BigDecimal valor;
    private BigDecimal valorImposto;

    public NotaFiscal(String nomeCliente, BigDecimal valor, BigDecimal valorImposto) {
        this.nomeCliente = Objects.requireNonNull(nomeCliente, "nome do cliente nao pode ser nulo");
        this.valor = Objects.requireNonNull(valor, "valor nao pode ser nulo");
        this.valorImposto = Objects.requireNonNull(valorImposto, "valor do imposto nao pode ser nulo");
    }

    public String getNomeCliente() {
        return nomeCliente;
    }

    public BigDecimal getValor() {
        return valor;
    }

    public BigDecimal getValorImposto() {
        return valorImposto;
    }

    @Override
    public String toString() {
        return "NotaFiscal{" +
                "nomeCliente='" + nomeCliente + '\'' +
                ", valor=" + valor +
                ", valorImposto=" + valorImposto +
                '}';
    }
}
