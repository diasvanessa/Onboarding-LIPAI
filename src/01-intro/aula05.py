""" Aula 05 - Tipos de Dados """

# 1 Numericos
# int, float, complex

idade = 27  # int
peso = 50.5  # float

print(idade, type(idade))
print(peso, type(peso))

# 2 Strings
nome = "Julio"  # str
sobrenome = "Silva"  # str
nome_completo = nome + " " + sobrenome  # concatenacao
print(nome_completo, type(nome_completo))

produto = "Coca-cola"

# O cliente nome_completo comprou o produto produto
print(f"O cliente {nome} {sobrenome} comprou o produto {produto}")

print(nome[0], nome[1], nome[-1])  # J u o

print(nome.lower())  # chama a funcao lower() - julio
print(nome.upper())  # chama a funcao upper() - JULIO

print(1, 3, 7, 9, "asdads", sep="      ")  # separador customizado

# 3 Booleanos

ligado = True
print(ligado, type(ligado))    # bool

# atribuir valor relacional ou logico

resultado = 10 < 3
print(resultado, type(resultado))  # False bool

# 4 Listas

frutas = ["banana", "maca", "laranja", "uva"]
print(frutas)
print(frutas[0])  # banana
print(frutas[1])  # maca
print(frutas[-1])  # uva
#print(frutas[5])   IndexError: list index out of range

# lista eh mutavel

frutas[0] = "banana prata"
frutas.append("abacaxi")  # adiciona elemento no final da lista
print(frutas)
print(len(frutas))  # tamanho da lista

for fruta in frutas:
    print(fruta.upper())  
    
# 5 Tuplas

codigos = ("MG01", "MG02", "MG03") 
print(codigos[0])  # MG01

# codigos[0] = "MG10" TypeError: 'tuple' object does not support item assignment

# codigos.append("MG04")  AttributeError: 'tuple' object has no attribute 'append'

print(len(codigos))  # tamanho da tupla

# 6 Conjuntos

resultados_sorteio = {10, 23, 45, 10, 5, 23, 67}
print(resultados_sorteio)  

resultados_sorteio.add(89)  # adiciona elemento ao conjunto
print(resultados_sorteio)

# 7 Dicionarios

funcionario = {
    "codigo": 1234,
    "nome": "Ana Paula",
    "salario": 3500.00
}
print(funcionario)
print(funcionario["codigo"])

print(funcionario.keys())    # chaves do dicionario
print(funcionario.values())  # valores do dicionario

funcionario["salario"] = 4000.00  # atualiza valor
print(funcionario)
