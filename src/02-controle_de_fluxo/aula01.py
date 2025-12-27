""" Aula 01 - Operadores """

# Operadores Aritméticos
n1 = 10.2  
n2 = 3.5
resultado = n1 + n2 + 8.5

print('1 + 1', 1 + 1, type( 1 + 1 ))  # Adição
print('1.2 + 1.1', 1.2 + 1.1, type( 1.2 + 1.1 ))  
print('resultado:', resultado, type( resultado ))
print('5 - 2', 5 - 2, type( 5 - 2 ))  # Subtração
print('5 * 2', 5 * 2, type( 5 * 2 ))  # Multiplicação
print('5 / 2', 5 / 2, type( 5 / 2 ))  # Divisão
print('3 % 2', 3 % 2, type( 3 % 2 ))  # Módulo - resto da divisao
print('5 // 2', 5 // 2, type( 5 // 2 ))  # Divisão Inteira
print('5 ** 2', 5 ** 2, type( 5 ** 2 ))  # Exponenciação

# Operadores de atribuicao
x = 10.0 # atribui valor 10.0 a x
print('x =', x, type(x))

# Operadores de comparacao
# avaliacao com boolean
resultado = x > 10
print('x > 10:', resultado, type( resultado ))

print('10 == 10:', 10 == 10, type( 10 == 10 )) # equal
print('10 != 10:', 10 != 10, type( 10 != 10 )) # not equal
print('10 > 10:', 10 > 10, type( 10 > 10 )) # greater than
print('10 >= 10:', 10 >= 10, type( 10 >= 10 )) # greater than or equal to
print('10 < 10:', 10 < 10, type( 10 < 10 )) # less than
print('10 <= 10:', 10 <= 10, type( 10 <= 10 )) # less than or equal to

# condicao = x < 10.0 and resultado < 3.0
# if condicao:
#     pass

# Operadores logicos

# AND
print('True and True:', True and True, type( True and True ))  
print('True and False:', True and False, type( True and False ))
print('False and False:', False and False, type( False and False ))  
print('False and True:', False and True, type( False and True ))

# OR
print('True or True:', True or True, type( True or True ))
print('True or False:', True or False, type( True or False ))
print('False or False:', False or False, type( False or False ))
print('False or True:', False or True, type( False or True ))

# NOT
condicao = False
print('not condicao:', not condicao, type( not condicao ))

# Operadores especiais

# is
# == comparar se dois valores sao iguais
# is verificar se as variaveis apontam para o mesmo 
# objeto na memoria

a=10
b=10.0
c = b

print(a == b, a==c, b==c) # True True True
print(a is b, a is c, b is c) # False False True

# in
# str, list, tuple, set, dic (chave)

frase = 'Voce eh um palavrao!'

print('palavrao' in frase,type('palavrao' in frase))  # palavrao esta na frase

numeros = [1, 5, 2, 4, 6]
print(10 in numeros)

numeros = (1, 5, 2, 4, 6)
print(5 in numeros)

numeros = {1, 5, 2, 4, 6}
print(3 in numeros)

pessoa = {
    'nome': 'Joao',
    'idade': 30
}

print('nome' in pessoa)
print('idade' in pessoa)  