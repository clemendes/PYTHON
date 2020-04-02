entradas = input().split()

s = int(entradas[0])
t = int(entradas[1])
f = int(entradas[2])

previsto = s + t + f

if previsto > 0 and previsto <=24:
	if previsto == 24:
		print(0)
	else:
		print(previsto)
elif previsto <0:
	print(24+previsto)
elif previsto > 24:
	print(previsto-24)
else:
  print(0)
