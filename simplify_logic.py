from sympy import *
a, b, c, d = symbols('a b c d')
simplify_logic((a | b))
simplify_logic((a | b) & (a|b) )
simplify_logic((a & b) | (a & b) )
simplify_logic((a & c) | (b & c) )
