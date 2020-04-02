# URI 1019
# CLEVERSON MENDES FARIA

segundos = int(input())

hora = int(segundos // 3600)             
minutos = int(((segundos % 3600)//60))
segundos = int((segundos % 3600) % 60)

print("%d:%d:%d" %(hora, minutos, segundos))
