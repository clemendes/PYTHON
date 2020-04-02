# URI 1021
# CLEVERSON MENDES FARIA

num = float(input())

#NOTAS
cem = num/100
cin = num%100/50
vin = num%50/20
dez = num%100%50%20/10
cinco = num%10/5
dois = num%5/2
#MOEDAS
um = num%100%50%20%10%5%2/1
cc = num%1/0.50
vc = num%0.50/0.25
dz = num%100%50%20%10%5%2%1%0.50%0.25/0.10
cincoc = num%100%50%20%10%5%2%1%0.50%0.25%0.10/0.05
umc = num%100%50%20%10%5%2%1%0.50%0.25%0.10%0.05/0.01+0.01

print("NOTAS:")
print("%d nota(s) de R$ 100.00" %cem)
print("%d nota(s) de R$ 50.00" %cin)
print("%d nota(s) de R$ 20.00" %vin)
print("%d nota(s) de R$ 10.00" %dez)
print("%d nota(s) de R$ 5.00" %cinco)
print("%d nota(s) de R$ 2.00" %dois)
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" %um)
print("%d moeda(s) de R$ 0.50" %cc)
print("%d moeda(s) de R$ 0.25" %vc)
print("%d moeda(s) de R$ 0.10" %dz)
print("%d moeda(s) de R$ 0.05" %cincoc)
print("%d moeda(s) de R$ 0.01" %umc)
