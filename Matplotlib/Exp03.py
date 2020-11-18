import numpy as np
import matplotlib.pyplot as plt

def h(x):
    return np.sin(x)

x = np.linspace(0, 10, 100)

plt.plot(x, h(x), label='seno')
plt.xlabel('tempo')
plt.ylabel('posicao')
plt.title('Funcao seno')
plt.grid()
plt.show()

