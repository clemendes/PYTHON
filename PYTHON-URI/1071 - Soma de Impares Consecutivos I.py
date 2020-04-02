# URI 1071
# CLEVERSON MENDES FARIA

x = int(input())
y = int(input())

#6 -5 = 5
#15 12 = 13
#12 12 = 0

soma =0

if (x > y):
    for i in range(y+1,x,1):
        if i % 2 != 0:
            soma += i

print(soma)
