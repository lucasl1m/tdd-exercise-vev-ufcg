class Funcionario:
    def __init__(self, nome, email, salario_base, cargo):
        self.nome = nome
        self.email = email
        self.salario_base = salario_base 
        self.cargo = cargo.upper() if cargo.upper() in ['DESENVOLVEDOR', 'DBA', 'TESTADOR', 'GERENTE'] else ''
    
    def get_salario(self):
        return self.salario_base
    
    def get_cargo(self):
        return self.cargo