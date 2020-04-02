# URI 1117
# CLEVERSON MENDES FARIA

cont = 0
nota1 = 0
nota2 = 0

while cont != 2:

    if cont < 1:
        nota1 = float(input())
        if nota1 >= 0 and nota1 <= 10:
            cont +=1
        else:
            print("nota invalida")

    if cont == 1:
        nota2 = float(input())
        if nota2 >= 0 and nota2 <= 10:
            cont +=1
        else:
            print("nota invalida")
            
media = (nota1+nota2)/2
print("media = %.2f" %media)
