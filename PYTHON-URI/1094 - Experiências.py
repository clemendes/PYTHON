# URI 1094
# CLEVERSON MENDES FARIA

n = int(input())

qtd_total = 0
coelhos = 0
ratos = 0
sapos = 0

for i in range(0,n,1):
  entrada = input().split()
  qtd = entrada[0]
  letra = entrada[1]

  qtd_total += int(qtd)

  if (letra == "C" or letra == "c"):
    coelhos += int(qtd)
  elif (letra == "R" or letra == "r"):
    ratos += int(qtd)
  elif (letra =="S" or letra == "s"):
    sapos += int(qtd)

print("Total: %d cobaias" %qtd_total)
print("Total de coelhos: %d" %coelhos)
print("Total de ratos: %d" %ratos)
print("Total de sapos: %d" %sapos)

p_coelhos = float(coelhos/qtd_total*100)
p_ratos = float(ratos/qtd_total*100)
p_sapos = float(sapos/qtd_total*100)

print("Percentual de coelhos: %.2f %%" %p_coelhos)
print("Percentual de ratos: %.2f %%" %p_ratos)
print("Percentual de sapos: %.2f %%" %p_sapos)
