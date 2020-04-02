# URI 1116
# CLEVERSON MENDES FARIA

n = int(input())

for i in range(0,n,1):
    entradas = input().split()
    x = float(entradas[0])
    y = float(entradas[1])

    if (x < 0) or (( x >= 0) and (y == 0)):
        print("divisao impossivel")    
    else:
        divisao = float(x / y)
        print("%.1f" %divisao) 
