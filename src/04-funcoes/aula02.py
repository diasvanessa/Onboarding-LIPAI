""" Aula 04.02 – Argumentos """

# positional, keyword, default values

# declarar uma funcao que soma dois numeros


def somar(n1, n2):
    soma = n1 + n2
    return soma


def dividir(dividendo, divisor):
    return dividendo / divisor


# argumentos posicionais
print(somar(10, 3.5))
print(dividir(10, 2.0))
print('--------------')

# unpack list e tuplas
numeros = [10.0, 5.5]
print('somar numeros de uma lista', somar(numeros[0], numeros[1]))
print('somar numeros de uma lista', somar(*numeros))  # desembrulhar a lista - os tamanhos precisam ser iguais
print('--------------')

# unpack dict - chaves precisam ter o mesmo nome dos parametros da funcao
numeros = {
    'n1': 10.2,
    'n2': 5.3
}
# desembrulhar a lista - os tamanhos precisam ser iguais
print('somar numeros de um dict', somar(**numeros))
print('--------------')

# argumentos nomeados (keyword)
print(somar(n1=3.5, n2=10))
print(dividir(divisor=3.0, dividendo=10.0))

# Declaracao
# nome: saudacoes
# parametros: nome, saudacao
# retorno: string

def saudacoes(nome, saudacao='Oi'): # Default
    return f'{saudacao}, {nome}'

print(saudacoes('Maria', 'Bom dia'))
print(saudacoes('Pedro'))