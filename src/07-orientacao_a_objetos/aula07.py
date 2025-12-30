""" Aula 07.07 – Relacionamento entre classes """

class Endereco:
    def __init__(self, cep, numero):
        self.cep = cep
        self.numero = numero
        
    def __str__(self):
        return f'Endereco[cep = {self.cep}, numero = {self.numero}]'


class Pessoa:
    def __init__(self, cpf, nome, telefone): # incluir o endereco aqui
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.enderecos = [] # = [endereco]
        
    def add_enderecos(self, endereco):
        self.enderecos.append(endereco)
        
    def print_enderecos(self):
        print(self.nome)
        for endereco in self.enderecos:
            print(endereco)
        
    def __str__(self):
        return f'Pessoa[cpf = {self.cpf}, nome = {self.nome}, telefone = {self.telefone}]'

class Telefone:
    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero
    
    def __str__(self):
        return f'Telefone[ddd= {self.ddd}, telefone= {self.numero}]'
    

telefone = Telefone('11', '1111-1111')
# vai apontar para um objeto do tipo telefone
pessoa = Pessoa('1234545', 'Maria', telefone)
pessoa1 = Pessoa('1223377', 'Joao', telefone)
pessoa2 = Pessoa('45545454', 'Paulo', telefone)

pessoa.add_enderecos(Endereco('38408390', 686))
pessoa1.add_enderecos(Endereco('38410390', 923))

print(pessoa)
print(pessoa.cpf, pessoa.nome, pessoa.telefone, pessoa.enderecos)
print(pessoa.telefone.ddd, pessoa.telefone.numero)

print(pessoa1.cpf, pessoa1.nome, pessoa1.telefone, pessoa1.enderecos)

pessoa1.print_enderecos()
pessoa.print_enderecos()
pessoa2.print_enderecos()