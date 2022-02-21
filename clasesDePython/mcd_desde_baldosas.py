import numpy as np
from sympy import igcd
import sympy.ntheory as nt
import matplotlib.pyplot as plt
from celluloid import Camera
plt.style.use("dark_background")

if __name__ == '__main__':
    colores = ["yellow", "red", "orange", "gray", "pink"]
    a = int(input("Dame un entero a: "))
    b = int(input("Dame un entero b: "))
    d = igcd(a, b)
    divisores = nt.divisors(d)
    fig, ax = plt.subplots()

    for divisor in divisores:
        ax.set(xlim=(-0.01, a+0.01), ylim=(-0.01, b+0.01),
                xticks=range(0, a+1, divisor), yticks=range(0, b+1, divisor))
        ax.set_title(f"{divisor} | mcd({a}, {b}) = {d}", fontsize=30)
        ax.set_aspect('equal')
        ax.grid(True)
        plt.pause(5)
        for divisor in divisores:
            color = np.random.choice(colores)
            ax.plot([divisor, divisor],[0, divisor], color=color)
            ax.plot([0, divisor],[divisor, divisor], color=color)
        plt.pause(0.5)
    plt.show()


# # PARA VIDEO
#
# if __name__ == '__main__':
#     colores = ["yellow", "red", "orange", "gray", "pink"]
#     a = int(input("Dame un entero a: "))
#     b = int(input("Dame un entero b: "))
#     d = igcd(a, b)
#     divisores = nt.divisors(d)
#     fig, ax = plt.subplots()
#     camera = Camera(fig)
#
#     for divisor in divisores:
#         ax.set(xlim=(-0.01, a+0.01), ylim=(-0.01, b+0.01),
#                 xticks=range(0, a+1, divisor), yticks=range(0, b+1, divisor))
#         ax.set_title(f"{divisor} | mcd({a}, {b}) = {d}", fontsize=30)
#         ax.set_aspect('equal')
#         ax.grid(True)
#         plt.pause(2)
#         camera.snap()
#     for divisor in divisores:
#         color = np.random.choice(colores)
#         ax.plot([divisor, divisor],[0, divisor], color=color)
#         ax.plot([0, divisor],[divisor, divisor], color=color)
#     plt.pause(2)
#     camera.snap()
#     plt.show()
#
#     anim = camera.animate()
#     vid = anim.save("baldosas_y_mcd.mp4")
