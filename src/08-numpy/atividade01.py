import numpy as np
from numpy.random import default_rng
from time import process_time
import matplotlib.pyplot as plt

a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(a)
print(type(a))

b = np.zeros(shape=(5, 3, 6))  # 5 matrizes 4x6 preenchidas com zeros
print(b)

c = np.ones(shape=(2, 3))  # duas matrizes 3x3 preenchidas com uns
print(c)

vazio = np.empty(3)  # matriz 3x3 preenchida com lixo de memória
print(vazio)

array_range = np.arange(10)  # array de 0 a 9, start é 0 e stop é 10
print(array_range)
array_range = np.arange(0, 10, 2)  # array de 0 a 9, com step(pulo) de 2
print(array_range)

# array de 20 elementos, com valores entre 0 e 100
array_linear = np.linspace(0, 100, num=40, retstep=True)
print(array_linear)

print(b)
print(b.shape)  # mostra a forma da matriz
print(b.size)  # mostra o número de elementos da matriz
print(b.ndim)  # mostra o número de dimensões da matriz

print('------------------')
print('Transformando um array 1D em 2D')
a = np.array([1, 2, 3])
print(a.ndim)
print(a.shape)
print('------------------')
a21 = a[np.newaxis, :]  # vetor linha horizontal
print(a21.ndim)
print(a21.shape)
print(a21)
print('------------------')
a22 = a[:, np.newaxis]  # vetor coluna vertical
print(a22.ndim)
print(a22.shape)
print(a22)
print('------------------')

print("Concatenando arrays")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.concatenate([a, b])
d = np.concatenate([b, a])
print(c)
print(d)

print('------------------')
print("Consultando itens de uma array", )
a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],[11, 12, 13, 14, 15]])
print(a)
print('------------------')
maior_8 = a[a%2==0]  # consulta os itens maiores que 8
print(maior_8)

print('------------------')
print('Operacoes com arrays')
a= np.array([1, 2, 3])
print(a)
print(a.sum())  # soma dos itens do array
print(a.max())  # maior valor do array
print(a.min())  # menor valor do array
print(a.mean())  # média dos itens do array

print('------------------')
print('Gerando amostrar aleatorias')
rng = default_rng()
aleatorio = rng.integers(low=0, high=10, size=(2,4))  # gera 10 números inteiros aleatórios entre 0 e 100
print(aleatorio)

print('------------------')
print('Diferenca entre arrays e lista')
lista = [1, 2, 3] # uma lista pode conter itens de tipos diferentes
print(lista)
print(type(lista))
print('------------------')
a= np.array([1, 2, 3]) # todos os itens do array devem ser do mesmo tipo, diferente de uma lista
print(a)
print(type(a))

# em tempo de processamento, o array eh mais rapido

print('------------------')
print('Comparando o tempo de processamento entre arrays e listas')
lista_a = list(rng.integers(10,100,10000000))
lista_b = list(rng.integers(10,100,10000000))
c = []
t1 = process_time()
for i in range(len(lista_a)):
    c.append(lista_a[i] * lista_b[i])
t2 = process_time()
print(f'Tempo gasto para multiplicar os itens da lista: {t2-t1:.4f} segundos')

array_a = rng.integers(10,100,10000000)
array_b = rng.integers(10,100,10000000)

t1_array = process_time()
c = array_a * array_b
t2_array = process_time()
print(f'Tempo gasto para multiplicar os itens do array: {t2_array-t1_array:.4f} segundos')

print('------------------')
print('Gerando um gráfico de dispersão com arrays')
dados_x = rng.integers(20,size=30)
dados_y = rng.integers(12,size=30)

plt.scatter(dados_x, dados_y)
plt.show()