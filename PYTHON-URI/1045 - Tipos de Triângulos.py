# URI 1045
# CLEVERSON MENDES FARIA

entradas = input().split()
entradas = sorted(entradas, key=float, reverse = True)

a = float(entradas[0])
b = float(entradas[1])
c = float(entradas[2])

if (a >= b + c):
  print("NAO FORMA TRIANGULO")

elif (a*a == b*b + c*c):
  print("TRIANGULO RETANGULO")
  if (a == b and a == c):
    print("TRIANGULO EQUILATERO")
  elif (a == b or b == c or c == a):
    print("TRIANGULO ISOSCELES")

elif (a*a > b*b + c*c):
  print("TRIANGULO OBTUSANGULO")
  if (a == b and a == c):
    print("TRIANGULO EQUILATERO")
  elif (a == b or b == c or c == a):
    print("TRIANGULO ISOSCELES")

elif (a*a < b*b + c*c):
  print("TRIANGULO ACUTANGULO")
  if (a == b and a == c):
    print("TRIANGULO EQUILATERO")
  elif (a == b or b == c or c == a):
    print("TRIANGULO ISOSCELES")
