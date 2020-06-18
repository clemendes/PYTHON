saida = False

while (saida == False):
  entradas = input().split()
  if int(entradas[0]) > int(entradas[1]):
    print("Decrescente")
  elif int(entradas[1]) > int(entradas[0]):
    print("Crescente")
  elif int(entradas[0]) == int(entradas[1]):
    saida = True
