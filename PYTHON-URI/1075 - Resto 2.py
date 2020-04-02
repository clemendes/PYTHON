# URI 1075
# CLEVERSON MENDES FARIA

num = int(input())

#DIVISAO
if (num < 10000):
    for i in range(1,10000,1):
        if i % num == 2:
            print(i)
