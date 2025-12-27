""" Aula 03.02 – Tuplas """

# ordenadas
# imutaveis
# indexavel

# criacao da tupla
nomes = ('Maria', 'Pedro', 'Joao')
print(nomes, type(nomes))

# acessar elementos da lista
print(nomes[0])  # primeiro elemento
print(nomes[0:2])  # slice - do indice 0 ao 1 (2-1)
print(nomes[1:])  # do indice 1 ate o final
print(nomes[:3])  # do inicio ate o indice 2 (3-1)

# modificar elementos - nao e possivel por ser imutavel
# nomes[0] = 'Maria da Silva'

for nome in nomes:
    print(nome)
    
print('------------')
    
for i in range(len(nomes)):
    print(nomes[i])
    
nomes2 = 'ANA', 'MARCOS', 'AMELIA'
print(nomes2, type(nomes2))

# unpack

# nome1 = nomes2[0]
# print(nome1)

nome1, nome2, nome3 = nomes2 # se nao tiver 
# variavel pra cada tupla nao da pra fazer unpack dessa forma
print(nome1, nome2, nome3)

# juntar duas tuplas

todos_nomes = nomes + nomes2
print(todos_nomes)