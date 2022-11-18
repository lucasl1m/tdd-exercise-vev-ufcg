import pytest
from funcionario import *


# AVL Test Cases
def test_limits_calc_salario_liquido():
    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 3000.01, 'DESENVOLVEDOR')
    assert funcionario.calc_salario_liquido() == 2400.01

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 3000, 'DESENVOLVEDOR')
    assert funcionario.calc_salario_liquido() == 2400.00

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 2999.99, 'DESENVOLVEDOR')
    assert funcionario.calc_salario_liquido() == 2699.99

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 2000.01, 'DBA')
    assert funcionario.calc_salario_liquido() == 1500.01

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 2000, 'DBA')
    assert funcionario.calc_salario_liquido() == 1500.00

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 1999.99, 'DBA')
    assert funcionario.calc_salario_liquido() == 1699.99

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 2000.01, 'TESTADOR')
    assert funcionario.calc_salario_liquido() == 1500.01

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 2000, 'TESTADOR')
    assert funcionario.calc_salario_liquido() == 1500.00

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 1999.99, 'TESTADOR')
    assert funcionario.calc_salario_liquido() == 1699.99

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 5000.01, 'GERENTE')
    assert funcionario.calc_salario_liquido() == 3500.01

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 5000, 'GERENTE')
    assert funcionario.calc_salario_liquido() == 3500.00

    funcionario = Funcionario('qualquer-nome', 'qualquer-email', 4999.99, 'GERENTE')
    assert funcionario.calc_salario_liquido() == 3999.99

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