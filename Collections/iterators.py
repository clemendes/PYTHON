import os

os.system("cls")

lista_simples = [10,20,30,40,50,60]

# Iteração Forma Padrão
meu_iter = iter(lista_simples)

# Proximo iteração
print(next(meu_iter))

# Iterator através do FOR
for i in lista_simples:
   print(i)

while True:
   try:
      elemento = next(meu_iter)
      print(elemento)
   except StopIteration:
      break

# Implementando o Iterator - N elevado ao Quadrado
class MeuIterator:
   def __init__(self, max=0):
      self.max = max

   def __iter__(self):
      self.n = 0
      return self

   def __next__(self):
      if self.n <= self.max:
         resultado = self.n ** 2 
         self.n += 1
         return resultado
      else:
         raise StopIteration

for i in MeuIterator(5):
   print(i)

   

