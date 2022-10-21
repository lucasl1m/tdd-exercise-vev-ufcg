class Funcionario:
    def __init__(self, nome, email, salario_base, cargo):
        self.nome = nome
        self.email = email
        self.salario_base = salario_base if salario_base >= 0 else 0 
        self.cargo = cargo.upper() if cargo.upper() in ['DESENVOLVEDOR', 'DBA', 'TESTADOR', 'GERENTE'] else ''
    
    def get_salario(self):
        return self.salario_base
    
    def get_cargo(self):
        return self.cargo
    
    def calc_salario_liquido(self):
        if self.cargo == 'DESENVOLVEDOR':
            if self.salario_base >= 3000:
                return float(f'{self.salario_base * 0.8:.2f}')
            else:
                return float(f'{self.salario_base * 0.9:.2f}')
        elif self.cargo == 'DBA':
            if self.salario_base >= 2000:
                return float(f'{self.salario_base * 0.75:.2f}')
            else:
                return float(f'{self.salario_base * 0.85:.2f}')
        elif self.cargo == 'TESTADOR':
            if self.salario_base >= 2000:
                return float(f'{self.salario_base * 0.75:.2f}')
            else:
                return float(f'{self.salario_base * 0.85:.2f}')
        elif self.cargo == 'GERENTE':
            if self.salario_base >= 5000:
                return float(f'{self.salario_base * 0.7:.2f}')
            else:
                return float(f'{self.salario_base * 0.8:.2f}')
        else:
            return 0