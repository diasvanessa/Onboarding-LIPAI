# matplotlib

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 500)
y = np.cos(4*t)

plt.plot(t, y)
plt.title('Gráfico de uma função cosseno')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.show()
