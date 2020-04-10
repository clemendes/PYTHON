import os

os.system("cls")

# Declarando Ranges
# 05 elementos - um em um - Inicia no 1 até 5(exclusivo)
r1 = range(5)

# Inicia no 2(inclusivo) até 10(exclusivo)
r2 = range(2,10)

# De 0(inclusivo) até 100(excusivo) a cada 10 em 10
r3 = range(0,100,10)

# r1
for i in r1:
   print(i, end=' ')

# nova linha
print()

# r2
for i in r3:
   print(i, end=' ')

if __name__ == "__main__":

   print()
   palavra = input()

   # INVERSAO PALAVRA
   inversao = range(len(palavra)-1,-1,-1)

   for i in inversao:
     print(palavra[i], end="")
