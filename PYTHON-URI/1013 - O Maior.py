# URI 1013 - CLEVERSON MENDES FARIA - APRENDENDO PYTHON

import math

entradas = input().split()

#a,b,c = int(a),int(b),int(c)

a = int(entradas[0])
b = int(entradas[1])
c = int(entradas[2])

maiorAB = ((a+b+abs(a-b))/2)
maior = ((maiorAB+c+abs(maiorAB-c))/2)

maior = int(maior)

print(maior, "eh o maior")
