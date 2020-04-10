from array import array
import os

os.system("cls")

# Array do tipo Positivos
array_i = array('B', [1,2,3,4,5])
print("")
for i in array_i:
   print(i, end="|")

# Insert(2, 99) - Inserindo Elemento 99 no Array
array_i.insert(2,99)
print("")
for i in array_i:
   print(i, end="|")

# Remove(3) - Removendo Elemento do Array
array_i.remove(3)
print("")
for i in array_i:
   print(i, end="|")

# Index(99) - Buscar Elemento de um Array
print("")
print(array_i.index(99))

# Atribuição - Atualizando valor de um elemento
array_i[2] = 55

for i in array_i:
   print(i, end="|")