import os

os.system("cls")

# Nas Tuplas os dados armazenados não podem ser alterados

# Tupla = () Parenteses ou Sem
minha_tupla = (1, 2, 3, True, "Olá")
tupla2 = "X", "Y", "Z", 33, 44, True, False

print(type(minha_tupla))
print(type(tupla2))

# Count() - Qtd. ocorrências elementos em uma Tupla
print(minha_tupla.count(2))

# Index() - Posição do elemento na Tupla
print(minha_tupla.index(3))

# In - Verificar se existe elemento na Tupla
print(2 in minha_tupla)

# Concatenar Tuplas
print(minha_tupla.__add__(tupla2))

print(hash(tupla2))