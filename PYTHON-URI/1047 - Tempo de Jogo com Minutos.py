# URI 1047
# CLEVERSON MENDES FARIA

entradas = input().split()

hi = int(entradas[0])
mi = int(entradas[1])
hf = int(entradas[2])
mf = int(entradas[3])

ini = hi * 60 + mi
fim = hf * 60 + mf
duracao = 0

if (hi > hf):
    dif = (24*60 - ini) + fim
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %((dif - dif%60)/60,dif%60))
else:
    dif = fim - ini
    if(dif == 0):
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(24,dif%60))
    else:
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %((dif - dif%60)/60,dif%60))
