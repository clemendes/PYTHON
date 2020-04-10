import os

os.system("cls")

# Podemos Adicionar ou Remover, mas não Editar
# Sem repetições

# Declarando um Set
set1 = {1, 2, 3, 4}

# Declarando pelo Metodo Set do Python
set2 = set([4, 5, 6, 7, 8])
set3 = {3,5,11,15,18,20}

# Add() - Adicionar elementos no Set
set1.add(10)
print(set1)

# Update([]) - Inserir vários elementos
set1.update([3,4,9,10])
print(set1)

# Discard() - Remover elemento no Set
set1.discard(10)
print(set1)

# União elementos entre Sets
print(set1 | set2)

# Union()
print(set1.union(set3))

# Intersecção
print(set1 & set2)

# Intersection
print(set1.intersection(set3))

# Diferença
print(set1 - set2)

# Difference
print(set1.difference(set2))

# Diferençe Simétrica
print(set1 ^ set2)

# Symmetric Difference
print(set1.symmetric_difference(set3))