import matplotlib.pyplot as plt
import numpy as np

#t = np.arange(0,100)
t = np.linspace(0, 2*np.pi, 100)
#y = np.exp(t)
y= np.cos(t)
y1 = np.sin(t)

plt.figure("Grafico", figsize=(6, 6))
plt.plot(t, y, label="Cosseno")
plt.plot(t, y1, label="Seno")
plt.title("Grafico das funcoes seno e cosseno")
plt.xlabel("Eixo de Tempo")
plt.ylabel("Eixo de Amplitude")
plt.grid()
plt.show()
