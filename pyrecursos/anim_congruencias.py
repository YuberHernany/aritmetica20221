import numpy as np
import matplotlib.pyplot as plt
import sympy.ntheory as nt
from anim_divisibility_wih_points import VisualNumber

plt.style.use("dark_background")

if __name__ == '__main__':
    a = VisualNumber(30)
    b = VisualNumber(28)
    m = VisualNumber(4)
    fig, ax = plt.subplots(1,2)
    plt.subplot(121)
    ax = plt.gca()
    m.isDivisorOf(a)
    plt.subplot(122)
    ax = plt.gca()
    m.isDivisorOf(b)
    plt.show()




    # fig, ax = plt.subplots()
    # ax = plt.gca()
    # m.isDivisorOf(a)
    # r = a.number % m.number
    # print(f"Remember the residue is {r}")
    # plt.show()


    # fig, ax = plt.subplots()
    # ax = plt.gca()
    # m.isDivisorOf(b)
    # r = b.number % m.number
    # print(f"Remember the residue is {r}")
    # plt.show()
