import sympy as sy

# Gaussian sum
x, y, z, i, k, n = sy.symbols('x,y,z,i,k,n')
g_sum = sy.summation(i, (i, 1, n))
g_sum_res = n * (n + 1) / 2

print(g_sum.expand() == g_sum_res.expand())
# print(g_sum == g_sum_res) # .expand() no muta expresión
# siempre hay que expandir antes de comparar con ==
# simplificaciones no trabajan bien con flotantes (use enteros o Rationals)
# si se requiere, use sy.factorial

# for k in range(1, 11):
#     print(f"suma de Gauss hasta {k} es ", g_sum.subs({n:k}),"\n", f"fórmula de suma de Gauss evaluada en {k} es ", g_sum_res.subs({n:k}))

# expr.evalf() para un solo valor. expr.evalf(subs={a:val, b:val, etc})
# aunque lo mejor es crear funciones a partir de expresiones
# f = sy.lambdify(n, g_sum_res)
# print(f(3))

# tambien se peuden crear funciones a partir de expresiones de mas variables
# f = sy.lambdify((x,y,z), expr_de_x_y_z)

# sy.lambdify convierte las sy.functs en math.functs correspondientes, pero si se pasa el argumento "numpy"
# sy.lambdify convierte las sy.functs en np.functs que admiten argumentos de tipo ndarray
# siempre tenga como primera opción sy.lambdify y como segunda opción .subs o .evalf(subs={})

# sy.Derivative() y sy.Integral() son expresiones no evaluadas
# expr.diff(expr, var) expr.integrate(expr, var) son expresiones evaluadas inmediatamente


sy.init_printing()
print(sy.Rational(1,2) * x ** 2) # en jupyter notebook la salida es hermosa
# print(sy.latex(sy.log(x**(1/2))))
