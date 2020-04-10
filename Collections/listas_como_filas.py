from collections import deque
import os

os.system("cls")

minha_fila = deque(["João", "Pedro", "Augusto", "José"])

print(minha_fila)

# Popleft() - Removendo primeiro elemento da Fila
minha_fila.popleft()
print(minha_fila)

# Inserindo elementos 
minha_fila.append("Maria")
print(minha_fila)

