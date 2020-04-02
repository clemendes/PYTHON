entradas = input().split()
n1 = int(entradas[0])
n2 = int(entradas[1])

if n1 > n2:
    maior = n1
    print(maior)
elif n2 > n1:
    maior = n2
    print(maior)
else:
	print(n1)
