# URI 1165
# CLEVERSON MENDES FARIA

n = int(input())

for i in range(0,n,1):
  x = int(input())
  cont = 0
  for y in range(1,x+1,1):
    if x % y == 0:
      cont+= 1
      if cont > 2:
        print("%d nao eh primo" %x)
        break

  if cont == 2:
    print("%d eh primo" %x)
