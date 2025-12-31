""" Herança entre Classes – super() """

class Pessoa: # SUPER CLASSE
    def __init__(self, nome, sobrenome, cpf):
        #print('Entrei no SUPER CONSTRUTOR')
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def obtem_nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


class Cliente(Pessoa): # SUB CLASSE
    def __init__(self, pessoa):
        super().__init__(pessoa.nome, pessoa.sobrenome, pessoa.cpf)
        self.compras = []

# pessoa = Pessoa("Vanessa", "Ferreira", "123.123.123-12")
# cliente = Cliente(pessoa)
# print(cliente.obtem_nome_completo)    
# print(type(cliente))

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, salario):
        super().__init__(nome, sobrenome, cpf)
        self.salario = salario
        
    def calcular_pagamento(self):
        return self.salario - ((10/100) * self.salario)

    def __str__(self):
        return f'Nome: {super().obtem_nome_completo()}, Salario: {self.salario}'

class Programador(Funcionario):
    def __init__(self, nome, sobrenome, cpf, salario, bonus):
        super().__init__(nome, sobrenome, cpf, salario)
        self.bonus = bonus

    def calcular_pagamento(self):
        return super().calcular_pagamento() + self.bonus

# funcionario = Funcionario("Joao", "Silva", "124.124.124-12", 5600)
# print(funcionario)
# print(funcionario.calcular_pagamento())

programador = Programador("Joao", "Silva", "124.124.124-12", 5600, 200)
print(programador)
print(programador.calcular_pagamento())