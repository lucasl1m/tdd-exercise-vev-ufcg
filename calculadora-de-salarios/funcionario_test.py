from funcionario import *

def test_funcionario_init():
    funcionario = Funcionario('', '', 0, '')
    assert funcionario.nome == ''
    assert funcionario.email == ''
    assert funcionario.salario_base == 0
    assert funcionario.cargo == ''

def test_get_salario():
    funcionario = Funcionario('', '', 0, '')
    assert funcionario.get_salario() == 0

def test_get_cargo():
    funcionario = Funcionario('', '', 0, '')
    assert funcionario.get_cargo() == ''