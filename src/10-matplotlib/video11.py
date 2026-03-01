from matplotlib import pyplot as plt
import numpy as np

plt.style.use('ggplot')

x = np.linspace(1, 5, 500)
y = np.log10(x)

fig, axe = plt.subplots(figsize=(7, 4))
axe.plot(x, y, lw=1.2, color='blue', label='log10(x)')

axe.text(2.6, 0.35, 'P(2.5; 0.4)')
axe.text(3, 0.42, 'Logaritmo $y = log_{10}x$',
         fontsize=10,
         bbox=dict(boxstyle='round', facecolor='red', edgecolor='black', alpha=0.5))

axe.annotate('P(2.5; 0.4)', xy=(2.5, 0.4), xytext=(0.5, 0.62),
             fontsize=16, arrowprops=dict(facecolor="red", color = "red", shrink=0.05))

axe.plot([0, 2.5], [0.4, 0.4],
         color='black', linestyle='--', lw=0.8)

axe.plot([2.5, 2.5], [0, 0.4],
         color='black', linestyle='--', lw=0.8)

axe.plot(2.5, np.log10(2.5), marker='o', color='black')

axe.set_xticks(np.arange(0, 5.5, 0.5))

axe.set_title('Grafico logaritimico', fontsize=14, fontweight='bold')
axe.set_xlabel('x', fontsize=12)
axe.set_ylabel('log10(x)', fontsize=12)

plt.show()
