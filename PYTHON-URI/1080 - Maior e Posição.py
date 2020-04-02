# URI 1080

# CLEVERSON MENDES FARIA

n = int(input())
temp = 0

for i in range(1,100):
    num = int(input())
    if num > temp:
        maior = num
        posicao = i + 1
        temp = num

print(maior)
print(posicao)
