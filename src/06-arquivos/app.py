""" Aula 06.01 - Manipulando arquivos """

# r -leitura
# a - append / incrementar
# w - escrita
# x - criar arquivo
# r+ - leitura + escrita

# arquivo = open ("test.txt", "r")

# print(arquivo.readable()) # verificar se arquivo pode ser lido

# printa o arquivo - print(arquivo.read())
# print(arquivo.readline()) # itera na linha
# lista = arquivo.readlines() # transforma em lista

# print(lista)
# print(lista[1])

# arquivo = open ("test.txt", "a") # adiciona coisas no final do arquivo
# arquivo = open ("test.txt", "w") # limpa todo o arquivo

# arquivo.write("SQL\n")
# arquivo.write("C++\n")

# tambem eh possivel criar um novo arquivo
# arquivo = open ("test2.txt", "w")

# arquivo.write("SQL\n")
# arquivo.write("C++\n")

# arquivo = open ("test3.txt", "x")
# arquivo.write("SQL\n")

# arquivo.close # fechar arquivo no final

# Exclusao de arquivo

import os

# if os.path.exists("test2.txt"):
#     os.remove("test2.txt")  # tem q fechar o arquivo antes de excluir ele
# else:
#     print('Arquivo nao encontrado')

os.rmdir('src/06-arquivos/nova-pasta') # remove pasta se estiver vazia