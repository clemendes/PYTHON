# URI 1963
# CLEVERSON MENDES FARIA

import math

entradas = input().split()
a = float(entradas[0])
b = float(entradas[1])

if (a > 0.00) and (a <= 1000.00) and (b > 0.00) and (b <= 1000.00):
    diferenca = ((b - a)/a)*100
    print("%.2f%%" %diferenca)
