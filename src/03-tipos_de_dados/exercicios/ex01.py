"""
Solicite ao usuário 3 números.
○ Armazene os valores em uma lista.
○ Ao final, apresente o menor e o maior elemento.
"""

numeros = []

for i in range(3):
    numero = float(input(f"Digite o numero {i + 1}: "))
    numeros.append(numero)
    
print(numeros, type(numeros))

menor_numero = numeros[0]
maior_numero = numeros[0]

for numero in numeros:
    if numero < menor_numero:
        menor_numero = numero
    if numero > maior_numero:
        maior_numero = numero
        
print(f'O maior numero eh: {maior_numero} e o menor numero eh: {menor_numero}')