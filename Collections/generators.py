import os

os.system("cls")

# Generator (Yield)
def eleva_dois(max=0):
   n = 0
   while n <= max:
      yield n ** 2
      n += 1

for i in eleva_dois(5):
   print(i)

class Lista():

  def __init__(self):
     self.list = []

  def inserir(self, valor):
    self.list.append(valor)

  def items(self):
    n = 0
    max = len(self.list)
    while n < max:
      yield self.list[n]
      n += 1

# Aplicando Método GENERATOR
if __name__ == "__main__":

    lista = Lista()

    for item in input().split(' '):
        valor = int(item)
        lista.inserir(valor)

    iterador = lista.items()
    if "iterator" in iterador.__class__.__name__:
        print("O método não pode retornar um iterador")

    for valor in lista.items():
        print(str(valor), end=' ')