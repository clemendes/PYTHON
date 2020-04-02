# URI 1146
# CLEVERSON MENDES FARIA

x = True

while (x == True):
  n = int(input())
  
  v = []

  if (n == 0):
    x = False
  else:
    for i in range(1,n+1,1):
      v.append(i)
   
    print(*v, sep=" ")
