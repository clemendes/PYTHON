# URI 1020
# CLEVERSON MENDES FARIA

dias = int(input())

anos = int(dias // 365)             
meses = int(((dias % 365)//30))
dias = int((dias % 365) % 30)

print("%d ano(s)" %anos)
print("%d mes(es)" %meses)
print("%d dia(s)" %dias)
