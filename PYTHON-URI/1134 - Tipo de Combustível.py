# URI 1134
# CLEVERSON MENDES FARIA

n = 1

alc = 0
gas = 0
die = 0

while n != 4:

    n = int(input())

    if (n>=1) and (n<=4):
        if(n == 1):
            alc += 1
        elif (n==2):
            gas += 1
        elif (n==3):
            die +=1

print("MUITO OBRIGADO")
print("Alcool: %d" %alc)
print("Gasolina: %d" %gas)
print("Diesel: %d" %die)
