# URI 1159
# CLEVERSON MENDES FARIA

n = 1

while (n != 0):
    n = int(input())

    if n == 0:
        break

    cont = 0
    soma = 0
    num = n
    
    while cont < 5:
        if (num % 2 == 0):
            soma += num
            num += 1
            cont += 1
        else:
            num += 1

    print(soma)
