#!/usr/bin/env python3

from sympy import *

# создание переменных
x = symbols('x')
# y = symbols('y')

# задание уравнения
# equation = 2*log(x) + log(y) - 3*log(x*y) - log(16)

def log4(k):
    return log(k) / log(4)

equation = log4(5*x-4)-3/(log4(x*5-4)-1) + 1 

# упрощение уравнения
simplified_equation = simplify(equation)

# решение уравнения
solution = solve(simplified_equation, x)

# вывод результатов
print("Уравнение: ", equation)
print("Упрощенное уравнение: ", simplified_equation)
print("Решение уравнения: ", solution)
