# URI 1101
# CLEVERSON MENDES FARIA

x = True

while (x == True):
  n = input().split()
  n1 = int(n[0])
  n2 = int(n[1])
  v = []

  if (n1 <= 0 or n2 <= 0):
    x = False
  else:
    if (n1 > n2):
      soma = 0
     
      for i in range(n2,n1+1,1):
        soma += i
        v.append(i)

      v.append("Sum=%d" %soma)
    else:
      soma = 0
     
      for i in range(n1,n2+1,1):
        soma += i
        v.append(i)

      v.append("Sum=%d" %soma)

    print(*v, sep=" ")
