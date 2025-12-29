""" Aula 06.02 - Manipulando arquivos """

#arquivo = open("arquivo.txt", "w")

#string = "Ola, tudo bem?"
#lista = ["Ana\n", "Joao\n", "Maria\n", "Marcos\n"]

#arquivo.write(string) # uma string
#arquivo.writelines(lista) # varias string

# for nome in lista:
#     arquivo.write(nome)

# arquivo = open("arquivo.txt", "a")

# arquivo.close()

# with open("arquivo.txt", "w") as arquivo:
#     arquivo.write("teste")

# with open("arquivo.txt", "a") as arquivo:
#     arquivo.write("teste")

# with open("arquivo.txt", "r") as arquivo:
#     x = arquivo.read()
#     print(type(x))

# with open("arquivo.txt", "r") as arquivo: # gerador de contexto
#     x = arquivo.readlines()
#     print(type(x))
  
# with open("arquivo.txt", "rb") as arquivo: # estancia de um byte
#     x = arquivo.read()
#     print(x.decode())
 
# with open("arquivo.txt", "rb") as arquivo: # estancia de um byte
#     for i in arquivo: # linha por linha
#         print(i)
        
with open("arquivo.txt", "r") as arquivo:
    print(next(arquivo))
    print(next(arquivo))
  
print("fim")