# URI 1087
# CLEVERSON MENDES FARIA

while True:
    entradas = input().split()
    
    x1 = int(entradas[0])
    y1 = int(entradas[1])
    x2 = int(entradas[2])
    y2 = int(entradas[3])

    if (x1 + y1 + x2 + y2) == 0:
        break
    
    if (x1==x2) and (y1==y2):
        print("%d" %0)
        continue
    
    if (x1==x2) or (y1==y2):
        print("%d" %1)
        continue
    
    if abs(x1-x2) == abs(y1-y2):
        print("%d" %1)
        continue
    
    print("%d" %2)
