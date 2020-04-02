# URI 1066
# CLEVERSON MENDES FARIA

a = [0,0,0,0,0]

cont_pos = 0
cont_par = 0
cont_impar = 0
cont_neg = 0

a[0] = input()
a[1] = input()
a[2] = input()
a[3] = input()
a[4] = input()

for i in a:
    if int(i) % 2 == 0:
        cont_par += 1

    if int(i) % 2 != 0:
        cont_impar += 1

    if int(i) > 0:
        cont_pos += 1

    if int(i) < 0:
        cont_neg += 1

  
print("%d valor(es) par(es)" % cont_par)
print("%d valor(es) impar(es)" %cont_impar)
print("%d valor(es) positivo(s)" %cont_pos)
print("%d valor(es) negativo(s)" %cont_neg)
