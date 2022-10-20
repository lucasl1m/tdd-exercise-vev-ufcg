from funcionario import *

# Teste inicialização da classe Funcionario
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

    # Teste valor de cargo válido
    funcionario = Funcionario('', '', 0, 'DESENVOLVEDOR')
    assert funcionario.get_cargo() == 'DESENVOLVEDOR'

    # Teste valor de cargo captializado ou minúsculo
    funcionario = Funcionario('', '', 0, 'Gerente')
    assert funcionario.get_cargo() == 'GERENTE'

    # Teste valor de cargo inválido
    funcionario = Funcionario('', '', 0, 'PO')
    assert funcionario.get_cargo() == ''