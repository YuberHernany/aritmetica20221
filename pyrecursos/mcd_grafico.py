










import numpy as np
import matplotlib.pyplot as plt

def rect_de_puntos(x_min, x_max, y_min, y_max, **kwargs):
    xs, ys = np.meshgrid(np.arange(x_min, x_max + 1, 1),
                         np.arange(y_min, y_max + 1, 1))
    Xs, Ys = xs.ravel(), ys.ravel()
    ax = plt.gca()
    ax.scatter(Xs, Ys, s=0.5, **kwargs)


def maximocomundivisor(a, b):
    """
    input: a,b type integers
    output: list with two objects, first the mcd(a,b),
    second list of qotients in division algorithm
    """
    a1 = abs(a)
    b1 = abs(b)
    r1 = a1 % b1
    q1 = a1 // b1
    cocientes = [q1]
    residuos = [r1]
    if r1 > 0:
        r2 = 1
        while r2 != 0:
            r2 = b1 % r1
            q2 = b1 // r1
            cocientes.append(q2)
            residuos.append(r2)
            b1 = r1
            r1 = r2
        return [residuos, cocientes]
    else:
        return [[r1], [q1]]


if __name__ == '__main__':
    mensaje = """
    ingrese enteros a y b, se recomiendan valores como:

    opcion1
    a = 330
    b = 210

    opcion2
    a = 390
    b = 330

    opcion3
    a = 1001
    b = 275

    """

    primer_mensaje = "primero ingrese a: "
    segundo_mensaje = "ahora ingrese b: "


    a = int(input(mensaje+primer_mensaje))
    b = int(input(mensaje+segundo_mensaje))


    a = max(a, b)
    b = min(a, b)



    colores = ['red', 'yellow', 'green', 'blue', 'orange', 'gray', 'sienna',
                'tan', 'gold', 'darkcyan', 'mediumpurple', 'beige']

    fig, ax = plt.subplots()
    ax.set_title(f"el mcd({a}, {b}) es: {maximocomundivisor(a, b)[0][-2]}")
    ax.set(xlim=(-1, a+1), ylim=(-1, b+1))
    ax.set_aspect("equal")
    residuos, cocientes = maximocomundivisor(a, b)
    rect_de_puntos(1, a, 1, b, c='black')
    plt.pause(2)

    if len(cocientes) >= 1:
        for i in range(cocientes[0]):
            rect_de_puntos(1, (i+1)*b, 1, b, c=np.random.choice(colores))
            x_current = (i+1)*b
            y_current = 0
            plt.pause(1)
    if len(cocientes) >= 2:
        for i in range(cocientes[1]):
            rect_de_puntos(x_current, x_current+residuos[0],
                           y_current, y_current + residuos[0], c=np.random.choice(colores))
            # x_current = x_current
            y_current = (i+1)*residuos[0]
            plt.pause(1)
    if len(cocientes) >= 3:
        for i in range(cocientes[2]):
            rect_de_puntos(x_current, x_current+residuos[1],
                            y_current, y_current+residuos[1], c=np.random.choice(colores))
            x_current = x_current+residuos[1]
            # y_current = y_current
            plt.pause(1)
    if len(cocientes) >= 4:
        for i in range(cocientes[3]):
            rect_de_puntos(x_current, x_current+residuos[2],
                           y_current, y_current+ residuos[2], c=np.random.choice(colores))
            # x_current = x_current
            y_current = y_current+ residuos[2]
            plt.pause(1)
    if len(cocientes) >= 5:
        for i in range(cocientes[4]):
            rect_de_puntos(x_current, x_current+residuos[3],
                            y_current, y_current+residuos[3], c=np.random.choice(colores))
            x_current = x_current+residuos[3]
            # y_current = y_current
            plt.pause(1)

    if len(cocientes) >= 6:
        for i in range(cocientes[5]):
            rect_de_puntos(x_current, x_current+residuos[4],
                           y_current, y_current+ residuos[4], c=np.random.choice(colores))
            # x_current = x_current
            y_current = y_current+ residuos[4]
            plt.pause(1)
    if len(cocientes) >= 7:
        for i in range(cocientes[6]):
            rect_de_puntos(x_current, x_current+residuos[5],
                            y_current, y_current+residuos[5], c=np.random.choice(colores))
            x_current = x_current+residuos[5]
            # y_current = y_current
            plt.pause(1)


    plt.show()
