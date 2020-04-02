# URI 1060
# CLEVERSON MENDES FARIA

a = [0,0,0,0,0,0]
cont = 0

a[0] = input()
a[1] = input()
a[2] = input()
a[3] = input()
a[4] = input()
a[5] = input()

for i in a:
    if float(i) > 0:
        cont += 1

print("%d valores positivos" %cont)
