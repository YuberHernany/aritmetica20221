import numpy as np
import matplotlib.pyplot as plt
plt.style.use("dark_background")

ORIGEN = np.array([0,0])
k_s = np.arange(12)
puntos = np.array([[np.cos(2 * k * np.pi / 12), np.sin(2 * k * np.pi / 12)] for k in k_s]).reshape(-1, 2)
marcas = [3, 2, 1, 12, 11, 10, 9, 8, 7, 6, 5, 4]

fig, ax = plt.subplots()
ax.scatter(puntos[:, 0], puntos[:, 1], s=50, c='gray')
ax.set_aspect('equal')
ax.axis('off')
for marca, posicion in zip(marcas, 1.2 * puntos):
    ax.text(posicion[0] - 0.05, posicion[1], str(marca), fontsize=20)

a = int(input("Dame un entero que indica una 'hora': "))
b = int(input("Dame un entero que indica una 'hora': "))
index_de_a = marcas.index(a)
index_de_b = marcas.index(b)
suma = (a+b)%12
index_de_suma = marcas.index(suma)
for num, color in zip([a, b, suma], ['green', 'green', 'yellow']):
    k = marcas.index(num)
    ax.plot([0, 0.9 * puntos[k][0]], [0, 0.9 * puntos[k][1]], linewidth=5, color=color)

ax.plot()

plt.show()
