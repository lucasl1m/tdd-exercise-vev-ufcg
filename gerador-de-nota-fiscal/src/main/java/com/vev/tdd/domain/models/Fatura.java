package com.vev.tdd.domain.models;

import java.math.BigDecimal;
import java.util.Objects;

public class Fatura {
    private String nome;
    private String endereco;
    private String tipo;
    private BigDecimal valor;

    public Fatura(String nome, String endereco, String tipo, BigDecimal valor) {
        this.nome = Objects.requireNonNull(nome, "nome nao pode ser nulo");
        this.endereco = Objects.requireNonNull(endereco, "endereco nao pode ser nulo");
        this.tipo = Objects.requireNonNull(tipo, "tipo nao pode ser nulo");
        this.valor = Objects.requireNonNull(valor, "valor nao pode ser nulo");
    }

    public String getNome() {
        return nome;
    }

    public String getEndereco() {
        return endereco;
    }

    public String getTipo() {
        return tipo;
    }

    public BigDecimal getValor() {
        return valor;
    }
}
