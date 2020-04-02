# URI 1154
# CLEVERSON MENDES FARIA

idade = 0
soma = 0
cont = 0

while idade >= 0:
    idade = int(input())

    if idade >=0:
        soma += idade
        cont += 1
    
media = float(soma) / int(cont)

print("%.2f" %media)
