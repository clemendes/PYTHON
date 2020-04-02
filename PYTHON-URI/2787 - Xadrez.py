# URI 2787
# CLEVERSON MENDES FARIA

l = int(input())
c = int(input())

if (l >= 1) and (l <= 1000) and (c >= 1) and (c <= 1000):
    if (l + c) % 2 == 0:
        print(1)
    else:
        print(0)
