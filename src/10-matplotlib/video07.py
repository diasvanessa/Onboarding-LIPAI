from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 70)
y = np.cos(4*x)
print(y)

plt.figure(figsize=(8, 4)) # largura, altura

plt.plot(x, y, color = "black",
         label='Cosine', lw = 1.5,
         marker = 'o', linestyle = 'dashdot', 
         markersize = 5)
plt.title('Cosine Function')
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.grid()
plt.show()
