import numpy as np
import matplotlib.pyplot as plt

def h(x):
    return np.sin(x)

g = lambda x: np.cos(x)

v = [0, 10, -5, 5]

x = np.linspace(0, 10, 100)

plt.plot(x, h(x), 'r--', label='seno')
plt.plot(x, g(x), label='coseno')
plt.xlabel('tempo')
plt.ylabel('posicao')
plt.title('Funcoes trigonometricas')
plt.legend(loc=1)
plt.text(4, 0, 'prueba')
plt.axis(v)
plt.grid()
plt.show()

