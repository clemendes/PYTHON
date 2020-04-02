# URI 2808
# CLEVERSON MENDES FARIA

letras = ("x","a","b","c","d","e","f","g","h")
numeros = (1,2,3,4,5,6,7,8)
posicao1 = posicao2 = posicao3 = posicao4 = 0
movimento = 0
movimento1 = 0
movimento2 = 0

entradas = input().split()
ini = str(entradas[0])
fim = str(entradas[1])

letra1 = str(ini[0])
numero1 = int(ini[1])

letra2 = str(fim[0])
numero2 = int(fim[1])

for i in range(0,len(letras),1):
    if letra1 == letras[i]:
        posicao1 = i

for i in range(0,len(numeros),1):
    if numero1 == numeros[i]:
        posicao2 = i

for i in range(0,len(letras),1):
    if letra2 == letras[i]:
        posicao3 = i

for i in range(0,len(numeros),1):
    if numero2 == numeros[i]:
        posicao4 = i

# print(posicao1,posicao2,posicao3,posicao4)

if (posicao1 >= posicao3):
    movimento1 = (posicao1 - posicao3)
else:
    movimento1 = (posicao3 - posicao1)
    
if (posicao2 >= posicao4):
    movimento2 = (posicao2 - posicao4)
else:
    movimento2 = (posicao4 - posicao2)

movimento = movimento1 + movimento2

if (movimento == 3 ):
    print("VALIDO")
else:
    print("INVALIDO")


