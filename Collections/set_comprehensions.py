import os

os.system("cls")

# Definindo um Set com Compreehension
# Não é definido em ordem
set_comprehension1 = {i*i for i in range(0,10)}
print(set_comprehension1)

set1 = {1,2}
set2 = {3,4,5}

set_comprehension2 = {i for i in set1.union(set2)}
print(set_comprehension2)