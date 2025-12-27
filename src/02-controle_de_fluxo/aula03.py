""" Aula 02.03 - loop for """

# 1. Iterar sobre sequencias (strings, listas, tuplas, dicionarios, etc)
# 2. Repetir instrucoes

linguagens = ['Python', 'Java', 'JavaScript']

# print(linguagens[0])
# print(linguagens[1])
# print(linguagens[2])

# for valor in colecao:
#     instrucao
#     ...

# comportamento do operador 
# in eh diferente com base no contexto
print('Java' in linguagens)

for linguagem in linguagens:
    print(linguagem)
    
nota1 = 10.0
nota2 = 5.5
nota3 = 8.3

media = (nota1 + nota2 + nota3) / 3
print(f'Media: {media}')

# e se eu nao souber quantas notas tenho?
notas = [10.0, 5.5, 8.3] 
soma = 0

for nota in notas:
    soma += nota
    
media = soma / len(notas)
print(f'Media: {media}')

# range
# valores = range(10) # stop, assume iniciando em 0
# valores = range(0, 10) # start e stop
# valores = range(0, 10, 2) # start, stop e step
valores = range(9, -1, -1) # necessario definir step negativo

print(valores)

for valor in valores:
    print(valor)

# melhor para iterar sobre indices de listas
for linguagem in range(len(linguagens)):
    print(linguagens[linguagem])