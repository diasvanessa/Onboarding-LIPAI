import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 500)
y = np.cos(4*t)
y1 = np.sin(4*t)

plt.figure("Cosseno", figsize=(7, 6))
plt.plot(t, y)
plt.title('Gráfico de uma função cosseno')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')

plt.figure("Seno", figsize=(7, 5))
plt.plot(t, y1)
plt.title('Gráfico de uma função seno')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude ')

plt.show()

