""" Aula 04 - Variaveis, constantes e literais """

# Variavel container para guardar dados

numero = 10
print(numero, type(numero))  # int

# Inferencia de tipo
# Python identifica o tipo do dado automaticamente

numero = 20
print(numero, type(numero))  # int

# multiplas atribuicoes - nao recomendado

nome, idade, endereco = "Maria", 30, "Rua A, 123"
print(nome, idade, endereco)

nome = "Maria"
idade = 30
endereco = "Rua A, 123"
print(nome, idade, endereco)

# atribui mesmo valor a multiplas variaveis

nome1 = nome2 = nome3 = "Ana"  # nao e um ponteiro
print(nome1, nome2, nome3)

nome2 = "Beatriz"
print(nome1, nome2, nome3)

# Variaveis
# snake_case

id_funcionario = 209
salario_atual = 5000.50
print(id_funcionario, salario_atual)

# Constantes
# Upper case - snake_case

PI = 3.14159
MAIORIDADE_CIVIL = 21
MAIORIDADE_PENAL = 18

print(PI, MAIORIDADE_CIVIL, MAIORIDADE_PENAL)

# Literais
# Valores fixos atribuídos diretamente no código

idade = 27
print(idade)
print(27)

# Numericos

print(10, type(10))          # int
print(10,type(-10))         
print(3.14, type(3.14))      # float

# Strings
# aspas simples e aspas duplas sao equivalentes - escolher uma forma e usar consistentemente

print("Hello, World!", type("Hello, World!"))  # str
print('Python é ótimo!', type('Python é ótimo!'))  # str

print("John's book")  # Usando aspas duplas para incluir apostrofo
print('She said "Hello!"')  # Usando aspas simples para incluir aspas duplas

# Booleanos

print(True, type(True))    # bool
print(False, type(False))  # bool

# None

print(None, type(None))    # NoneType

# Colecoes

# Lista - list
numeros = [1, 2, 3, 4, 5]
print(numeros, type(numeros))

# Tuplas - tuple
emails = ('joao@email.com', 'maria@email.com')
print(emails, type(emails)) # tuplas sao imutaveis

# Conjuntos - set
jogos = {'mario', 'zelda', 'metroid'}
print(jogos, type(jogos)) # nao permite elementos duplicados e nao garante ordem

# Dicionarios - dict\
# conjuntos de pares chave:valor
aluno = {
    'prontuario': 12345,
    'nome': 'Carlos Silva',
    'idade': 21
}
print(aluno, type(aluno))