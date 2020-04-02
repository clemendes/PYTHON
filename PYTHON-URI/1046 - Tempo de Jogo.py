# URI 1046
# CLEVERSON MENDES FARIA

entradas = input().split()

a = int(entradas[0])
b = int(entradas[1])

if a == b:
    dif = 24
    
if b < a:
    dif = (24 - a) + b
elif b > a:
    dif = b - a

print("O JOGO DUROU %d HORA(S)" %dif)
