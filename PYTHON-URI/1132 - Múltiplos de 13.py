# URI 1132
# CLEVERSON MENDES FARIA


a = int(input())
b = int(input())
soma = 0

if a < b:
    for i in range(a,b+1,1):
        if (i % 13 != 0):
            soma += i
else:
    for j in range(b,a+1,1):
        if (j % 13 != 0):
            soma += j
    
print("%d" %soma)
