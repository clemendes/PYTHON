entradas = input().split()

a = int(entradas[0])
b = int(entradas[1])

if a > b:
  if a%b==0:
    print("Sao Multiplos")
  else:
    print("Nao sao Multiplos")
else:
  if b%a==0:
    print("Sao Multiplos")
  else:
    print("Nao sao Multiplos")
