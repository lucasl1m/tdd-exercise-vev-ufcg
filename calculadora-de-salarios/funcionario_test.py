import pytest
from funcionario import *

def test_valid_params_funcionario_init():
    funcionario = Funcionario('', '', 0, '')
    assert funcionario.nome == ''
    assert funcionario.email == ''
    assert funcionario.salario_base == 0
    assert funcionario.cargo == ''

def test_invalid_params_funcionario_init():
  with pytest.raises(TypeError):
    funcionario = Funcionario()
    funcionario = Funcionario('', '', 0 )
    funcionario = Funcionario('', '', 0, '')

def test_invalid_params_get_salario():
    funcionario = Funcionario('', '', -1, '')
    assert funcionario.get_salario() == 0

def test_invalid_params_get_cargo():
    funcionario = Funcionario('', '', 0, '')
    assert funcionario.get_cargo() == ''

    funcionario = Funcionario('', '', 0, 'PO')
    assert funcionario.get_cargo() == ''

def test_valid_params_get_cargo():
    funcionario = Funcionario('', '', 0, 'DESENVOLVEDOR')
    assert funcionario.get_cargo() == 'DESENVOLVEDOR'

    funcionario = Funcionario('', '', 0, 'Gerente')
    assert funcionario.get_cargo() == 'GERENTE'

def test_valid_calc_salario_liquido():
    funcionario = Funcionario('', '', 7000, 'DESENVOLVEDOR')
    assert funcionario.calc_salario_liquido() == 5600.00

    funcionario = Funcionario('', '', 2900, 'DESENVOLVEDOR')
    assert funcionario.calc_salario_liquido() == 2610.00

    funcionario = Funcionario('', '', 2000, 'DBA')
    assert funcionario.calc_salario_liquido() == 1500.00

    funcionario = Funcionario('', '', 1900, 'DBA')
    assert funcionario.calc_salario_liquido() == 1615.00

    funcionario = Funcionario('', '', 3000, 'TESTADOR')
    assert funcionario.calc_salario_liquido() == 2250.00

    funcionario = Funcionario('', '', 1999, 'TESTADOR')
    assert funcionario.calc_salario_liquido() == 1699.15

    funcionario = Funcionario('', '', 4000, 'GERENTE')
    assert funcionario.calc_salario_liquido() == 3200.00

    funcionario = Funcionario('', '', 5000, 'GERENTE')
    assert funcionario.calc_salario_liquido() == 3500.00

def test_invalid_calc_salario_liquido():
    funcionario = Funcionario('', '', 4000, 'PO')
    assert funcionario.calc_salario_liquido() == 0

    funcionario = Funcionario('', '', 2000, 'DBA')
    assert funcionario.calc_salario_liquido() != 1700.00

    funcionario = Funcionario('', '', 0, '')
    assert funcionario.calc_salario_liquido() == 0