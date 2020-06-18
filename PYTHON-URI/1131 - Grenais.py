j= 0
i = 0
g = 0
e = 0

while True:
	entradas = input().split()
	gi = entradas[0]
	gg = entradas[1]
	j+=1
	if (gi > gg):
		i+=1
	elif (gg > gi):
		g+=1
	else:
		e+=1
	o = input("Novo grenal (1-sim 2-nao)\n")
	if (int(o)==2):
		break

print("%d grenais" %j)
print("Inter:%d" %i)
print("Gremio:%d" %g)
print("Empates:%d" %e)
if (i > g):
	print("Inter venceu mais")
elif (g > i):
	print("Gremio venceu mais")
else:
	print("Nao houve vencedor")
