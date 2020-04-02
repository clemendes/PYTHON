# URI 1043
# CLEVERSON MENDES FARIA

medidas = input().split()

a = float(medidas[0])
b = float(medidas[1])
c = float(medidas[2])

if (a < b + c) and (b < a + c) and (c < a + b):
    perimetro = a+b+c
    print("Perimetro = %.1f" %perimetro)
else:
    area = ((a + b) / 2)*c
    print("Area = %.1f" %area)
