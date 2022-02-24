import numpy as np
import matplotlib.pyplot as plt
import sympy.ntheory as nt
plt.style.use("dark_background")
plt.rc("text", usetex=True)
fig, ax = plt.subplots()
ax.set(xlim=(-2,2), ylim=(-2,2), xticks=(), yticks=(),)
n = int(input("Give me an integer n > 1: "))
n_dict = nt.factorint(n)
descomposicion_str = ""
for base, exponente in n_dict.items():
    descomposicion_str += str(base) + "^{" + str(exponente) + "}"
if len(str(n)) <= 8:
    ax.text(-1.8, 0, r"$"+str(n)+ " = " + descomposicion_str+"$", fontsize=80)
elif 8 < len(str(n)) <= 16:
    ax.text(-1.8, 0, r"$"+str(n)+ " = " + descomposicion_str+"$", fontsize=40)
elif 16 < len(str(n)):
    ax.text(-1.8, 0, r"$"+str(n)+ " = " + descomposicion_str+"$", fontsize=20)


plt.show()
