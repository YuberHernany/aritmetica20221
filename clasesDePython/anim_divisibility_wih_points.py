import numpy as np
import matplotlib.pyplot as plt
import sympy.ntheory as nt
from sympy import sieve

plt.style.use("dark_background")

ORIGIN = np.array([0, 0]).reshape(1, 2)
RIGHT =  np.array([1, 0]).reshape(1, 2)
UP =  np.array([0, 1]).reshape(1, 2)
LEFT = -RIGHT
DOWN = -UP

class VisualNumber:
    def __init__(self, number):
        """ number must be an object type int """
        self.number = number
        self.asarray = self.asarray()
    def __str__(self):
        return str(self.number)
    def asarray(self):
        col1 = np.linspace(1, self.number, self.number).reshape(-1, 1)
        col2 = np.zeros_like(col1)
        return np.hstack([col1, col2])
    def showNumber(self, loc=1, **kwargs):
        arr = self.asarray + loc * UP
        ax = plt.gca()
        ax.scatter(arr[:, 0], arr[:, 1], **kwargs)
    def isDivisorOf(self, other):
        a = self.number
        b = other.number
        if b == 0:
            print('Yes, 0 is multiple of all integer number')
        elif a == 0:
            print("Not interesting casee")
        else:
            q, r = b // a, b % a
            for i in range(1, q+1):
                ax = plt.gca()
                self.showNumber(loc=i, color='white')
            (VisualNumber(r)).showNumber(loc=q+1, color='red', label=f"residue = {r}")
            if r == 0:
                ax = plt.gca()
                ax.set(xticks=range(1, a+1), ylim=(0, q+5), yticks=range(1, q+1))
                ax.set_title(f"{a} is divisor of {b}, because residue is 0")
                plt.legend(loc="upper right")
            elif r != 0:
                ax = plt.gca()
                ax.set_title(f"{a} is not divisor of {b}, because residue {r} is different than 0")
                ax.set(xticks=range(1, a+1), ylim=(0, q+5), yticks=range(1, q+1))
                plt.legend(loc="upper right")
    def isPrime(self):
        p = self.number
        s = int(round(np.sqrt(p)) + 1)
        value_boolean = nt.isprime(p)
        if value_boolean:
            non_divisors = [VisualNumber(n) for n in sieve.primerange(s)]
            fig, axes = plt.subplots(1, len(non_divisors))
            for i, non_div in zip(range(len(axes)), non_divisors):
                plt.subplot(int("1"+str(len(axes))+str(i+1)))

            # for a, non_div in zip(axes, non_divisors):
                ax = plt.gca()
                non_div.isDivisorOf(self)
            plt.show()

        else:
            divisor = VisualNumber(nt.divisors(p)[-2])
            fig, ax = plt.subplots()
            ax = plt.gca()
            divisor.isDivisorOf(self)
            plt.legend(f"{p} is not a prime")
            plt.show()

        return value_boolean
        # return value_boolean

if __name__ == '__main__':

    plt.style.use("dark_background")
    fig, ax = plt.subplots()
    a = int(input("Give me the potential divisor or integer a: "))
    b = int(input("Give me the potential multiple or integer b: "))
    VisualNumber(a).isDivisorOf(VisualNumber(b))
    plt.show()
    ##     PARA VER SI UN NUMERO ES PRIMO
    vis_num = VisualNumber(130)
    print(vis_num.isPrime())
