""" Aula 03.03 – Set """

# nao ordenado
# mutaveis
# nao indexaveis
# nao aceitam elementos duplicados

# criar um set
numeros = {1, 2, 6, 7, 4, 11, 25, 7, 1}
print(numeros, type(numeros))

for numero in numeros:
    print(numero)
    
print(1 in numeros)
print(3 in numeros)

# adicionar itens ao set
print(numeros)
numeros.add(56)
print(numeros)

# adicionar elementos de um set em outro
numeros2 = {24, 2, 34, 654, 223,11}
print('----------')
print(numeros)
print(numeros2)

numeros.update(numeros2)
print(numeros, type(numeros))