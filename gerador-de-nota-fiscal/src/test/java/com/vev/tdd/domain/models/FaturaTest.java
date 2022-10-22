package com.vev.tdd.domain.models;

import org.junit.jupiter.api.Test;

import java.math.BigDecimal;

import static org.junit.jupiter.api.Assertions.*;

class FaturaTest {
    @Test
    void testParametrosNulos() {
        Throwable exception = assertThrows(NullPointerException.class, () -> new Fatura(
                null,
                null,
                null,
                null)
        );
        assertEquals("nome nao pode ser nulo", exception.getMessage());

        exception = assertThrows(NullPointerException.class, () -> new Fatura(
                "qualquer-nome",
                null,
                null,
                null)
        );
        assertEquals("endereco nao pode ser nulo", exception.getMessage());

        exception = assertThrows(NullPointerException.class, () -> new Fatura(
                "qualquer-nome",
                "qualquer-endereco",
                null,
                null)
        );
        assertEquals("tipo nao pode ser nulo", exception.getMessage());

        exception = assertThrows(NullPointerException.class, () -> new Fatura(
                "qualquer-nome",
                "qualquer-endereco",
                "qualquer-tipo",
                null)
        );
        assertEquals("valor nao pode ser nulo", exception.getMessage());
    }

    @Test
    void testParametrosCorretos() {
        Fatura fatura = new Fatura(
                "qualquer-nome",
                "qualquer-endereco",
                "qualquer-tipo",
                BigDecimal.valueOf(100)
        );
    }
}