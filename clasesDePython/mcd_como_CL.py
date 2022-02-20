import numpy as np
import matplotlib.pyplot as plt

plt.style.use("dark_background")



def maximocomundivisor(a, b):
    """
    input: a,b type integers
    output: list with two objects, first the mcd(a,b), second list of qotients in division algorithm
    """
    a1 = abs(a)
    b1 = abs(b)
    r1 = a1 % b1
    q1 = a1 // b1
    cocientes = [q1]
    if r1 > 0:
        r2 = 1
        while r2 != 0:
            r2 = b1 % r1
            q2 = b1 // r1
            cocientes.append(q2)
            b1 = r1
            r1 = r2
        return [b1, cocientes]
    else:
        return [b1, cocientes]


def mcd_CL(a,b):
    """
    input: integers a and b
    output: list of two integers, scalars for express mcd(a,b) as C.L
    """
    x0 = 0
    x1 = 1
    y0 = 1
    cocientes = maximocomundivisor(a,b)[1]
    y1 = -cocientes[0]
    n = len(cocientes)
    for i in range(1,n-1):
        x2 = x0 - x1 * cocientes[i]
        y2 = y0 - y1 * cocientes[i]
        x0 = x1
        x1 = x2
        y0 = y1
        y1 = y2
    return [x1, y1]



if __name__ == '__main__':
    # a = 1001
    # b = 275

    # a=2*3*5*13
    # b=2*3*5*11

    a = int(input("Dame el valor de a: "))
    b = int(input("Dame el valor de b: "))

    print(mcd_CL(a, b))

    # a y b se reservan a eje horizontal
    # x e y al vertical

    escalares = mcd_CL(a, b)
    semi_eje_hor = max(abs(a), abs(b))
    x, y = escalares[0], escalares[1]
    semi_eje_ver = max(abs(x), abs(y))

    fig, ax = plt.subplots()
    ax.set(xlim=(-semi_eje_hor-5, semi_eje_hor+5),
           ylim=(-semi_eje_ver-5, semi_eje_ver+5))
    ax.plot([-semi_eje_hor-3, semi_eje_hor+3], [0,0], color='gray')
    ax.plot([0,0], [-semi_eje_ver-3, semi_eje_ver+3], color='gray')
    ax.scatter([a, b], [0, 0], c='white')
    ax.scatter([0, 0], [x, y], c='yellow')
    def coloracion(A, B):
        if A * B > 0:
            return 'green'
        else:
            return 'red'
    ax.fill_between([0, a], [0, 0], [x, x], color=coloracion(a, x), alpha=0.5)
    ax.fill_between([0, b], [0, 0], [y, y], color=coloracion(b, y), alpha=0.5)
    ax.text(a, 1, f'a={a}', fontsize=30)
    ax.text(b, 1, f'b={b}', fontsize=30)
    ax.text(-1, x, f'x={x}', fontsize=30)
    ax.text(-1, y, f'y={y}', fontsize=30)
    ax.text(a/2, x/2, f'ax={a*x}')
    ax.text(b/2, y/2, f'by={b*y}')
    ax.set_title(f"ax+by = ({a})({x}) + ({b})({y})={a*x+b*y}", fontsize=40)


    plt.show()
