import pandas as pd
import numpy as np
import sympy.ntheory as nt
from sympy.core import igcd
import sys
sys.path.append("/home/yuber/Documentos/1UdeA/xAritmetica/arit_6am/programas")
from primos_criterios import solu_particular_ecu_diofantica


if __name__ == "__main__":
    def solu_general_ecu_diofantica(a, b, c, n_sols):
        solu_particular = solu_particular_ecu_diofantica(a, b, c)
        if type(solu_particular) != type(None):
            x0, y0 = solu_particular[0], solu_particular[1]

            def solucion_t(t):
                x = x0 + int(b // igcd(a, b)) * t
                y = y0 - int(a // igcd(a, b)) * t
                return [x, y]
        else:
            print("No hay soluciones")
            return None
        return np.array([solucion_t(t) for t in range(-n_sols, n_sols + 1)]).reshape(-1, 2)


    primer_mensaje = """ Para resolver la ecuacion Diofantica tipo ax+by=c, ingresarás los coeficientes uno a uno
     y luego el número de soluciones que deseas"""

    print(primer_mensaje)
    a = int(input("Dame el coeficiente a: "))
    b = int(input("Dame el coeficiente b: "))
    c = int(input("Dame el coeficiente c: "))
    n_sols = int(input("Dame el número de soluciones que quieres: "))

    print(" las soluciones son: ")
    print(pd.DataFrame(solu_general_ecu_diofantica(a, b, c, n_sols // 2), columns=['x', 'y']))
