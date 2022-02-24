import numpy as np
import matplotlib.pyplot as plt
import sympy.ntheory as nt
import math
plt.style.use("dark_background")
plt.rc("text", usetex=True)

if __name__ == '__main__':
    def fontsize_dependiendo_de_n(n):
        if len(str(n)) <= 8:
            return 80
        elif 8 < len(str(n)) <= 16:
            return 40
        elif 16 < len(str(n)):
            return 20


    def info_de_n(n, loc):
        n_dict = nt.factorint(n)
        descomposicion_str = ""
        for base, exponente in n_dict.items():
            descomposicion_str += str(base) + "^{" + str(exponente) + "}"
        ax.text(-1.8, loc, r"$"+str(n)+ " = " + descomposicion_str+"$", fontsize=fontsize_dependiendo_de_n(n))


    fig, ax = plt.subplots()
    n = int(input("Dame el tamaño de la laguna de primos: "))
    ax.set(xlim=(-2,2), ylim=(0,n), xticks=(), yticks=(),)
    for i, m in enumerate(range(math.factorial(n+1)+2, math.factorial(n+1) + n+2)):
        ax = plt.gca()
        info_de_n(m, i)

    plt.show()
