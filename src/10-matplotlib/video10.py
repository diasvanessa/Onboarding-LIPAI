from matplotlib import pyplot as plt
import numpy as np

plt.style.use('ggplot')

x = np.linspace(1, 5, 500)
y = np.log10(x)

fig, axe = plt.subplots(figsize=(7, 4))
axe.plot(x, y, lw=1.2, color='blue', label='log10(x)')

# identificar um ponto especifico no grafico, quero enfatizar o ponto onde x= 2.5
# riscar uma linha horizontal no valor de y correspondente a x=2.5, ou seja, log10(2.5)
axe.plot([0, 2.5], [0.4, 0.4],
         color='black', linestyle='--', lw = 0.8)  # x, y

# riscar uma linha vertical no valor de x=2.5, ou seja, log10(2.5)
axe.plot([2.5, 2.5], [0, 0.4],
         color='black', linestyle='--', lw = 0.8)  # x, y

axe.plot(2.5, np.log10(2.5), marker='o', color='black')  # x, y

axe.set_xticks(np.arange(0, 5.5, 0.5))

plt.show()
