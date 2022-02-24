import numpy as np
import matplotlib.pyplot as plt
plt.style.use("dark_background")
ORIGEN = np.array([0,0])
k_s = np.arange(28)
puntos = np.array([[np.cos(2 * k * np.pi / 28), np.sin(2 * k * np.pi / 28)] for k in k_s]).reshape(-1, 2)
marcas_letras = 'a b c d e f g h i j k l m n ñ o p q r s t u v w x y z #'.split(" ")
marcas_num = "0 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27".split(" ")

clave = int(input("Dame un entero positivo entre 1 y 27 como clave para encriptar: "))
clave_descifrar = 28 - clave
theta = 2 * np.pi / 28
matrix_rotation = np.array([[np.cos(clave * theta), np.sin(clave * theta)],
                            [-np.sin(clave * theta), np.cos(clave * theta)]]).reshape(-1, 2)
puntos_rotados = puntos @ matrix_rotation
fig, ax = plt.subplots()
ax.set(xlim=(-2.2, 2.2), ylim=(-1.4, 1.4))
ax.scatter(puntos[:, 0], puntos[:, 1], s=50, c='gray')
ax.set_aspect('equal')
ax.axis('off')
for marca, posicion in zip(marcas_letras, 1.2 * puntos):
    ax.text(posicion[0] - 0.05, posicion[1], str(marca), fontsize=20)
for marca, posicion in zip(marcas_num, 0.9 * puntos):
    ax.text(posicion[0] - 0.05, posicion[1], str(marca), fontsize=20)
for marca, posicion in zip(marcas_letras, 1.3 * puntos_rotados):
    ax.text(posicion[0] - 0.05, posicion[1], str(marca), fontsize=20, color='green')


ax.plot([0, 0.7 * puntos[clave][0]], [0, 0.7 * puntos[clave][1]], linewidth=5)

mensaje = "las#matematicas#requieren#disciplina"

def cifrar(plano):
    plano_separado = [letra for letra in plano]
    nuevos_indices = [(marcas_letras.index(letra) + clave) % 28 for letra in plano_separado]
    nuevas_letras = [marcas_letras[i] for i in nuevos_indices]
    cifrado = ""
    for letra in nuevas_letras:
        cifrado += letra
    return cifrado

mensaje_cifrado = cifrar(mensaje)

ax.text(-1.5, 1.5, mensaje, fontsize=16, color='gray')
ax.text(-1.5, -1.5, mensaje_cifrado, fontsize=16, color='gray')


plt.show()
