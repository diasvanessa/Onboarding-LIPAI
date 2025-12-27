""" Aula 04.01 – Introdução a funções """

# Funcao eh um bloco que realiza uma tarefa especifica
# Dividir o problema em pequenas partes 
# Evitar duplicacao de codigo

# 1. Standard library funcions - built-in functions
#  ex: print, len

print('ola', 123, True)

nomes = ['Joao', 'Maria']
tamanho_lista = len(nomes)
print(nomes, tamanho_lista)

# 2. User defined functions 
# definidas pelo desenvolvedor
# fazerem parte da solucao do problema

# declaracao
# nome: saudacoes
# parametros: nenhum
# retorno: nenhum
# def saudacoes():
#     print('ola')
    
# Chamada
# saudacoes()

# declaracao
# nome: saudacoes
# parametros: nome da pessoa
# retorno: nenhum

def saudacoes(nome):
    print(f'ola, {nome}')
    
# Chamada
# valores, variaveis, expressoes => argumentos
saudacoes('Vanessa') # argumento passado para o parametro nome
nome = 'Ana'
saudacoes(nome)

# declaracao
# nome: calcular_media
# parametros: nota1, nota2, nota3
# retorno: nenhum
# def calcular_media(nota1, nota2, nota3):
#     soma = nota1+nota2+nota3
#     media = soma / 3
#     print(media)

# Chamada
# argumentos sao literais
# calcular_media(10.0, 9.0, 3.9)
# n1 = 10.0
# n2 = 3.0
# n3 = 8.0
# calcular_media(n1, n2, n3)

# declaracao
# nome: calcular_media
# parametros: nota1, nota2, nota3
# retorno: media
def calcular_media(nota1, nota2, nota3):
    soma = nota1+nota2+nota3
    media = soma / 3
    return media

media = calcular_media(10.0, 9.0, 3.9)
print(media)

n1 = 10.0
n2 = 3.0
n3 = 8.0
media = calcular_media(n1, n2, n3)
print(media)

# enviar no email
# salvar no banco de dados
# salvar no arquivo