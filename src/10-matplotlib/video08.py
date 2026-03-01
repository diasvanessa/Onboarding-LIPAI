from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 300)
y = np.cos(3*x)

fig, axe = plt.subplots(figsize=(7, 4))

axe.plot(x, y)
axe.set_title('Grafico do Cosseno', fontsize=16)
axe.set_xlabel('Eixo x', fontsize=16)
axe.set_ylabel('Eixo y', fontsize=16)

plt.xticks(np.arange(0, 2*np.pi+0.4, 0.4))
plt.yticks(np.arange(-1, 1.3, 0.3))

plt.grid()
plt.show()