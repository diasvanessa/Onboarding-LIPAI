""" Aula 03.01 - Listas """

# ordenadas
# mutaveis
# indexadas

# criacao de lista
nomes = ['Joao', 'Maria', 'Jose', 'Ana']
print(nomes, type(nomes))

# acessar elementos da lista
print(nomes[0])  # primeiro elemento
print(nomes[0:2])  # slice - do indice 0 ao 1 (2-1)
print(nomes[1:])  # do indice 1 ate o final
print(nomes[:3])  # do inicio ate o indice 2 (3-1)

# modificar elementos da lista
nomes[1] = 'Maria da Silva'
nomes[2:] = ['Pedro da Silva', 'Carla Souza']
print(nomes)

# tamanho da lista
# funcao len
tamanho = (len(nomes))
print(tamanho)

# adicionar elementos na lista

# metodo append
nomes.append('Marcos Vieira')  # adiciona no final
print(nomes)

# metodo insert - vai deslocar pra posicao seguinte
nomes.insert(0, 'Guilherme Tavares')
print(nomes)

nomes.insert(2, 'Lucia Ferreira')
print(nomes)

# metodo extend - colocar elementos de uma lista dentro de outra

nomes2 = ['Caio Tavares', 'Julio Cezar']
print(len(nomes))
nomes.extend(nomes2)
print(len(nomes))
print(nomes)

# remover elementos

# remove

nomes.remove('Julio Cezar') # passa o valor que quer remover da lista
print(nomes)

# del

del nomes[0] # remover o valor que ta na posicao 0 
print(nomes)

# remove da memoria
# del nomes

# limpar a lista
# metodo clear
#nomes.clear()
#print(nomes)

# iteracao em lista
for nome in nomes: 
    print(nome)
    
print('-------------')
    
for i in range(len(nomes)):
    print(nomes[i])