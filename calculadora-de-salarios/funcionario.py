from cargos import cargos

class Funcionario:
    def __init__(self, nome, email, salario_base, cargo):
        if (nome == '' or email == '' or salario_base < 0 or cargo == '' or cargo.upper() not in cargos):
            raise ValueError( 'Invalid parameters' )

        self.nome = nome
        self.email = email
        self.salario_base = salario_base
        self.cargo = cargo.upper()
        
    
    def get_salario(self):
        return self.salario_base
    
    def get_cargo(self):
        return self.cargo
    
    def calc_salario_liquido(self):

        if ( cargos[self.cargo]['limite'] <= self.salario_base ):
            return self.salario_base - (self.salario_base * (cargos[self.cargo]['desconto1']))
        else:
            return self.salario_base - (self.salario_base * (cargos[self.cargo]['desconto2']))
