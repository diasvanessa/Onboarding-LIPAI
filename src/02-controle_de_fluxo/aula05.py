""" Aula 02.05 - break e continue """

# break - parar instrucao de loop
print("--- break ---")
for i in range(10):
    if i == 4:
        break # quebra o loop, vai imprimir so ate o 3
    # print(i)
    
# encontrar a posicao de um numero
# em uma lista de numeros, caso nao encontre
# posicao eh igual a -1    

busca = 5
numeros = [1, 3, 7, 9, 5, 11, 15]
posicao = -1

contador = 0 
for numero in numeros:
    print('Procurando na posicao: ', contador)
    if numero == busca:
        posicao = contador
        break
    contador += 1
    
print(f"Posicao do numero {busca}: {posicao}")

# for i in range(len(numeros)):
#     print('Procurando na posicao: ', i)
#     if numeros[i] == busca:
#         posicao = i
#         break    
# print(f"Posicao do numero {busca}: {posicao}")

# continue - pular a iteracao atual do loop
print("--- continue ---")
for numero in numeros:
    if numero == 3:
        continue # vai pular o 3
    print(numero)

