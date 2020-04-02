# URI 1149
# CLEVERSON MENDES FARIA

n = list(map(int, input().split()))
i = 1
soma = 0

while n[i] <= 0:
    if n[i] <=0:
        i = i + 1
    if n[i] > 0:
        break

for y in range(0,n[i]):
    soma = soma + n[0] + y
    
print(soma)
