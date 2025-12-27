"""
EX04
Crie uma função que recebe varios argumentos numericos atraves
de *args e retorna a soma dos numeros.
"""

def somar(*args):
    soma = 0
    for numero in args:
        soma += numero
    return soma

numeros = [10, 20, 30, 20, 10, 200, 1000, 50.4]
resultado_soma = somar(*numeros)
print(resultado_soma)