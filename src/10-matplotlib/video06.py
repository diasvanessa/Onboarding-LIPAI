import matplotlib.pyplot as plt
import numpy as np

# dados
x = np.arange(0, 5, 0.1)

# funções
y1 = x**2
y2 = x**5

# subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 4))
plt.suptitle('Subplots')
plt.subplots_adjust(wspace=0.5, hspace=0.64)

axes[0, 0].plot(x, y1)
axes[0, 0].set_title('y = x^2')
axes[0, 0].set_xlabel('Tempo')
axes[0, 0].set_ylabel('Valor')
axes[0, 0].grid()

axes[0, 1].plot(x, y2)
axes[0, 1].set_title('y = x^5')
axes[0, 1].set_xlabel('Tempo')
axes[0, 1].set_ylabel('Valor')
axes[0, 1].grid()

axes[1, 0].plot(x, y1)
axes[1, 0].set_title('y = x^2')
axes[1, 0].set_xlabel('Tempo')
axes[1, 0].set_ylabel('Valor')
axes[1, 0].grid()

axes[1, 1].plot(x, y2)
axes[1, 1].set_title('y = x^5')
axes[1, 1].set_xlabel('Tempo')
axes[1, 1].set_ylabel('Valor')
axes[1, 1].grid()

plt.show()
