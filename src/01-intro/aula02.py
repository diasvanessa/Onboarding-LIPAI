""" Aula 02 - Keywords e Identificadores """

# Palavras reservadas (keywords) nao podem ser usadas como identificadores
# True, False, None, and, import, lambda

# Identificadores
# nome de variaveis, funcoes, classes
# case sensitive (diferenciam maiusculas de minusculas)
# devem iniciar com letra ou underscore (_)
# nao pode ter espacos em branco ou caracteres especiais (ex: @, $, %, !)

nome = "Joao"
idade = 25

nome.upper()  # Metodo para deixar o nome em maiusculo

Nome = "Maria"  # Variavel diferente de 'nome'
nome_completo = "Maria da Silva"  # Uso de underscore para separar palavras

# Clean Code - Boas praticas

contador = 10  # Nome explicito
soma = 5 + 3  # Nome explicito
x = 5  # Nome nao explicito

# Constantes
# Em Python, por convencao, constantes sao escritas em maiusculas

PI = 3.14

idade = 15
MAIORIDADE = 18

if idade >= MAIORIDADE:
    print("Maior de idade")
else:
    print("Menor de idade")
