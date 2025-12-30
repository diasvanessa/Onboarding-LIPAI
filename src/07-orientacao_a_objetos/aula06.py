""" Aula 07.06 – __eq__ e __hash__ """

nome1 = 'Joao'
nome2 = 'Joao'

print(nome1 == nome2)

class Pessoa:
    def __init__(self, cpf, nome):
        self.nome = nome
        self.cpf = cpf
    
    # colecoes vai trabalhar usando equals
    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.cpf == value.cpf
        return False
    
    def __hash__(self):
        return hash(self.cpf)
    
    def __repr__(self):
        return f'Pessoa({self.cpf}, {self.nome})'
        
pessoa1 = Pessoa('100100100-10', 'Joao')
pessoa2 = Pessoa('100100100-10','Joao')
pessoa3 = Pessoa('100100100-11','Maria')

pessoas = {pessoa1,pessoa2,pessoa3}
print(pessoas)
print(pessoa1 == pessoa2)

pessoas_lista = [pessoa1,pessoa2,pessoa3]
print(pessoas_lista.count(pessoa1))