# URI 1064
# CLEVERSON MENDES FARIA

a = [0,0,0,0,0,0]
cont = 0

a[0] = input()
a[1] = input()
a[2] = input()
a[3] = input()
a[4] = input()
a[5] = input()

soma = 0

for i in a:
    if float(i) > 0:
        cont += 1
        soma += float(i)

if soma > 0:
    media = soma / cont
else:
    media = 0
    
print("%d valores positivos" %cont)
print("%.1f" %media)
