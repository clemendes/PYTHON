# URI 1079
# CLEVERSON MENDES FARIA

n = int(input())


for i in range(0,n,1):
  entradas = input().split()
  n1 = float(entradas[0])
  n2 = float(entradas[1])
  n3 = float(entradas[2])

  media = (((n1*2) + (n2*3) + (n3*5))/(2+3+5))

  print("%.1f" %media)
