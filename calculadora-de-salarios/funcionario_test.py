from funcionario import *

def test_funcionario_init():
    funcionario = Funcionario('', '', 0, '')
    assert funcionario.nome == ''
    assert funcionario.email == ''
    assert funcionario.salario_base == 0
    assert funcionario.cargo == ''
    

