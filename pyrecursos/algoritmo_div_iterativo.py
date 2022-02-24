# Algoritmo iterativo






















import numpy as np
import matplotlib.pyplot as plt
# import sys
# sys.path.append("")
from anim_divisibility_wih_points import VisualNumber

if __name__ == '__main__':
    a = int(input("Dame el valor de a: "))
    b = int(input("Dame el valor de b: "))
    a_visual = VisualNumber(a)
    b_visual = VisualNumber(b)

    fig, ax = plt.subplots()

    q = a // b
    r = a - b*q
    r_visual = VisualNumber(r)
    fig, ax = plt.subplots()
    ax.set(xlim=(0, b+1), ylim=(0, q+3))
    for i in range(q+1):
        b_visual.showNumber(loc=i, color='gray', alpha=0.3)
        r_visual.showNumber(loc=q+1, color='gray', alpha=0.3)
    plt.pause(2)
    for i in range(q+1):
        b_visual.showNumber(loc=i, color='white')
        plt.pause(2)
        r_visual.showNumber(loc=q+1, color='gray', alpha=0.3)

    plt.show()
