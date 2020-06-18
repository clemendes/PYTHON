n = int(input())

for i in range(0,n,1):
  total = 0
  entradas = input().split()
  if int(entradas[0]) > int(entradas[1]):
    maior = int(entradas[0])
    menor = int(entradas[1])
  else:
    maior = int(entradas[1])
    menor = int(entradas[0])

  for j in range(menor+1,maior,1):
    if j%2!=0:
      total += j

  print(total)
                         
