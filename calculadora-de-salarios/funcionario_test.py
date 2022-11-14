import pytest
from funcionario import *


# AVL Test Cases
def test_limits_calc_salario_liquido():
    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 3001, 'DESENVOLVEDOR')
    assert funcionario.calc_salario_liquido() == 2400.80

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 3000, 'DESENVOLVEDOR')
    assert funcionario.calc_salario_liquido() == 2400.00

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 2999, 'DESENVOLVEDOR')
    assert funcionario.calc_salario_liquido() == 2699.10

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 2001, 'DBA')
    assert funcionario.calc_salario_liquido() == 1500.75

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 2000, 'DBA')
    assert funcionario.calc_salario_liquido() == 1500.00

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 1999, 'DBA')
    assert funcionario.calc_salario_liquido() == 1699.15

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 2001, 'TESTADOR')
    assert funcionario.calc_salario_liquido() == 1500.75

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 2000, 'TESTADOR')
    assert funcionario.calc_salario_liquido() == 1500.00

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 1999, 'TESTADOR')
    assert funcionario.calc_salario_liquido() == 1699.15

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 5001, 'GERENTE')
    assert funcionario.calc_salario_liquido() == 3500.70

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 5000, 'GERENTE')
    assert funcionario.calc_salario_liquido() == 3500.00

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 4999, 'GERENTE')
    assert funcionario.calc_salario_liquido() == 3999.20

# Test Equivalence Partitions
def test_equivalence_calc_salario_liquido():
    with pytest.raises(ValueError):
        funcionario = Funcionario('', 'qualquer-email', 6000, 'DESENVOLVEDOR')
        funcionario = Funcionario('qualquer-nome', '', 6000, 'DESENVOLVEDOR')
        funcionario = Funcionario('qualquer-nome', 'qualquer-email', -1, 'DESENVOLVEDOR')
        funcionario = Funcionario('qualquer-nome', 'qualquer-email', 6000, '')
    
    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 6000, 'DESENVOLVEDOR')
    assert funcionario.calc_salario_liquido() == 4800.00

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 1500, 'DBA')
    assert funcionario.calc_salario_liquido() == 1275.00

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 6000, 'TESTADOR')
    assert funcionario.calc_salario_liquido() == 4500.00

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 1500, 'GERENTE')
    assert funcionario.calc_salario_liquido() == 1200.00

#Decision Table Test Cases 
def test_decision_table_calc_salario_liquido():
    with pytest.raises(ValueError):
        funcionario = Funcionario('', 'qualquer-email', 6000, 'DESENVOLVEDOR')
        funcionario = Funcionario('qualquer-nome', '', 6000, 'DESENVOLVEDOR')
        funcionario = Funcionario('qualquer-nome', 'qualquer-email', -1, 'DESENVOLVEDOR')
        funcionario = Funcionario('qualquer-nome', 'qualquer-email', 6000, '')
        funcionario = Funcionario('qualquer-nome', 'qualquer-email', 0, 'qualquer-cargo')

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 6000, 'DESENVOLVEDOR')
    assert funcionario.calc_salario_liquido() == 4800.00

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 6000, 'DBA')
    assert funcionario.calc_salario_liquido() == 4500.00

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 6000, 'TESTADOR')
    assert funcionario.calc_salario_liquido() == 4500.00

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 6000, 'GERENTE')
    assert funcionario.calc_salario_liquido() == 4200.00

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 1500, 'DESENVOLVEDOR')
    assert funcionario.calc_salario_liquido() == 1350.00

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 1500, 'DBA')
    assert funcionario.calc_salario_liquido() == 1275.00

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 1500, 'TESTADOR')
    assert funcionario.calc_salario_liquido() == 1275.00

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 1500, 'GERENTE')
    assert funcionario.calc_salario_liquido() == 1200.00


