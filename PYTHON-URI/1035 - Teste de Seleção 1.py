# URI 1035
# CLEVERSON MENDES FARIA

entradas = input().split()

A = int(entradas[0])
B = int(entradas[1])
C = int(entradas[2])
D = int(entradas[3])

if (B > C) and (D > A) and ((C + D) > (A + B)) and (C and D > 0) and (A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
