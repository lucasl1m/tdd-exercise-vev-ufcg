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

