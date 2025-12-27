""" EX03 - Crie um programa que solicite um identificador ao usuário e
informe se é válido ou inválido 
○ o código identificador contém 7 caracteres;
○ começa com BR;
○ seguido de um número inteiro entre 0001 e 9999;
○ por fim, termina com o caractere X.
○ Exemplos válidos: BR0001X, BR1236X, BR9999X
○ Exemplos inválidos: br0001X, BR126X, BR99999X, BR9999Y
"""

identificador = input('Digite o identificador: ')

valido = True

if len(identificador) != 7:
    valido = False
elif identificador[0:2] != 'BR':
    valido = False
else:
    numero = identificador[2:6]
    if numero.isdigit() == False:
        valido = False
    elif int(numero) < 1 or int(numero) > 9999:
        valido = False
    elif identificador[6] != 'X':
        valido = False

if valido:
    print('Identificador válido!')
else:
    print('Identificador inválido!')
