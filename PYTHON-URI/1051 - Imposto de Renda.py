sal = float(input())
imp = 0.00
faixa4 = 0.00
faixa3 = 0.00
faixa2 = 0.00

if sal <= 2000.00:
	print("Isento")
else:
	if sal >= 4500.01:
		faixa4 = sal - 4500.01
		imp += (0.28*faixa4)
		faixa3 = sal - faixa4 - 3000.01
		imp += (0.18*faixa3)
		faixa2 = sal - faixa4 - faixa3 - 2000.01
		imp += (0.08*faixa2)
		print('R$ %.2f' %imp)
	elif sal >= 3000.01:
		faixa3 = sal - faixa4 - 3000.01
		imp += (0.18*faixa3)
		faixa2 = sal - faixa4 - faixa3 - 2000.01
		imp += (0.08*faixa2)
		print('R$ %.2f' %imp)
	elif sal >= 2000.01:
		faixa2 = sal - faixa4 - faixa3 - 2000.01
		imp += (0.08*faixa2)
		print('R$ %.2f' %imp)
