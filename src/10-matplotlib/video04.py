import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 500)
c = np.cos(x)
s = np.sin(x)

plt.figure("Graficos de Seno e Cosseno", figsize=(8, 4)) # nome da figura e tamanho
plt.subplots_adjust(
    left = 0.152,
    right=0.943,
    top = 0.9,
    bottom=0.14,
    wspace= 0.345,
    hspace = 0.4
    ) # ajuste do espaço entre os gráficos

ax1 = plt.subplot(1, 2, 1) # linha, coluna, posicao
plt.plot(x, c)
ax1.set_title('Cosine') # titulo do grafico
ax1.set_xlabel('Eixo de tempo') # nome do eixo x
ax1.set_ylabel('Eixo de amplitude') # nome do eixo y
ax1.grid() # grade do grafico

ax2 = plt.subplot(1, 2, 2)
plt.plot(x, s)
ax2.set_title('Sine')
ax2.set_xlabel('Eixo de tempo') # nome do eixo x
ax2.set_ylabel('Eixo de amplitude') # nome do eixo y
ax2.grid() # grade do grafico

# ax3 = plt.subplot(2, 2, 3)
# plt.plot(x, c)

# ax4 = plt.subplot(2, 2, 4)
# plt.plot(x, s)

plt.show()