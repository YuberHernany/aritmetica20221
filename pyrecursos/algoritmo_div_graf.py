

























# El algoritmo de la division
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    plt.style.use("dark_background")

    a = int(input("Dame el dividendo: "))
    b = int(input("Dame el 'divisor': "))
    rational = a/b
    quotient_integer = int(np.floor(rational))
    residue = int(a - b * quotient_integer)

    print(quotient_integer)
    print(residue)


    fig, ax = plt.subplots()
    ax.set_title(f"Al dividir a={a} entre b={b}, q={quotient_integer} y r=a-bq={residue}", fontsize=40)
    ax.set(xlim=(quotient_integer-2, quotient_integer+2),
            ylim=(-1/2, 1/2), yticks=(),
            xticks=())
    ax.plot([quotient_integer-2, quotient_integer+2], [0,0], color='gray', alpha=0.5, linewidth=20)
    ax.scatter(np.arange(quotient_integer-2, quotient_integer + 3),
                [0,0,0,0,0], color='gray', alpha=0.5, linewidth=20)
    ax.scatter([rational], [0], color='yellow', marker='o', s=40)
    ax.scatter([quotient_integer], [0], color='green', marker='o', s=40)
    for num in range(quotient_integer-3, quotient_integer+4):
        plt.text(num, -0.05, str(num), fontsize=20)

    ax.annotate(xy=(rational, 0),
                xytext=(rational, -0.35),
                text=f"a/b={np.round(rational, 2)}",
                color='yellow',
                arrowprops=dict(facecolor='yellow', shrink=0.05),
                fontsize=30)
    ax.annotate(xy=(quotient_integer, 0),
                xytext=(quotient_integer, 0.35),
                text=f"q={quotient_integer}",
                color='green',
                arrowprops=dict(facecolor='green', shrink=0.05),
                fontsize=30)

    plt.show()
