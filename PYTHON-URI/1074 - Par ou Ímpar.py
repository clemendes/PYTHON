# URI 1074
# CLEVERSON MENDES FARIA

n = int(input())

for i in range(1,n+1,1):
    valor = int(input())
    if (valor % 2 == 0 and valor > 0):
      print("EVEN POSITIVE")
    elif (valor % 2 != 0 and valor > 0):
      print("ODD POSITIVE")
    if (valor % 2 == 0 and valor < 0):
      print("EVEN NEGATIVE")
    elif (valor % 2 != 0 and valor < 0):
      print("ODD NEGATIVE")
    elif (valor == 0):
      print("NULL")
