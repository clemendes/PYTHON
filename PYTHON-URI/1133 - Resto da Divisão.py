# URI 1133
# CLEVERSON MENDES FARIA

a = int(input())
b = int(input())

if a>b:
    for i in range(b+1,a,1):
        if (i % 5 == 2) or (i % 5 == 3):
            print(i)
            
elif b>a:
    for j in range(a+1,b,1):
        if (j % 5 == 2) or (j % 5 == 3):
            print(j)
