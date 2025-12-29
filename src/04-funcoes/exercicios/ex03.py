"""
EX03
Crie uma funcao que recebe uma tupla de numeros como
parametro (numeros) e retorna a soma desses numeros.
"""

def somar(n1, n2, n3):
    return n1 + n2 + n3

breakpoint()
numeros = {10, 20, 30}
resultado_soma = somar(*numeros)
print(resultado_soma)

