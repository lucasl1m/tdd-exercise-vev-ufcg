package com.vev.tdd.domain.models;

import org.junit.jupiter.api.Test;

import java.math.BigDecimal;

import static org.junit.jupiter.api.Assertions.*;

class NotaFiscalTest {
    @Test
    void testParametrosNulos() {
        Throwable exception = assertThrows(NullPointerException.class, () -> new NotaFiscal(
                null,
                null,
                null)
        );
        assertEquals("nome do cliente nao pode ser nulo", exception.getMessage());

        exception = assertThrows(NullPointerException.class, () -> new NotaFiscal(
                "qualquer-nome",
                null,
                null)
        );
        assertEquals("valor nao pode ser nulo", exception.getMessage());

        exception = assertThrows(NullPointerException.class, () -> new NotaFiscal(
                "qualquer-nome",
                BigDecimal.valueOf(100),
                null)
        );
        assertEquals("valor do imposto nao pode ser nulo", exception.getMessage());
    }

    @Test
    void testParametrosCorretos() {
        NotaFiscal notaFiscal = new NotaFiscal(
                "qualquer-nome",
                BigDecimal.valueOf(100),
                BigDecimal.valueOf(0)
        );
    }
}