import matplotlib.pyplot as plt
import numpy as np

x= np.arange(0,5,0.1)
print(x)
y1= x**2
y2 = x**5

# subplots
fig, ((ax1,ax2), (ax3,ax4)) = plt.subplots(nrows =2 , ncols = 2, figsize=(8,4))
plt.suptitle('Subplots')
plt.subplots_adjust(wspace=0.5, hspace=0.5)

ax1.plot(x,y1)
ax1.plot(x,y2)
ax1.set_xlabel('Tempo')
ax1.set_ylabel('Valor')
ax1.grid()

ax2.plot(x,y2)
ax2.plot(x,y2)
ax2.set_xlabel('Tempo')
ax2.set_ylabel('Valor')
ax2.grid()

ax3.plot(x,y1)
ax3.plot(x,y2)
ax3.set_xlabel('Tempo')
ax3.set_ylabel('Valor')
ax3.grid()

ax4.plot(x,y2)
ax4.plot(x,y2)
ax4.set_xlabel('Tempo')
ax4.set_ylabel('Valor')
ax4.grid()

plt.show()