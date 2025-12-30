""" Aula 07.02 – Atributos de instância e de classe """

# Classe Pessoa possui
# atributos de instancia: nome e email
# atributos de classe: especie

class Pessoa:
    especie = 'Humano'

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


pessoa1 = Pessoa('Vanessa', 'vanessa@mail.com')
pessoa2 = Pessoa('Julia', 'julia@mail.com')

# alterar um atributo de classe na instancia(objeto)
# altera somente para aquela instancia
pessoa2.especie = 'Alienigena'

# alterando um atributo de classe na classe
# altera todos os objetos e na classe tambem
Pessoa.especie = 'Alienigenas do Passsado'

print(pessoa1.nome, pessoa1.email, pessoa1.especie)
print(pessoa2.nome, pessoa2.email, pessoa2.especie)

print(Pessoa.especie)
