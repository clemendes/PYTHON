# URI 1759
# CLEVERSON MENDES FARIA

n = int(input())

sequencia = ""
for i in range(n):
    sequencia += ("Ho")
    if i == (n-1):
        sequencia += ("!")
    else:
        sequencia += (" ")
print(sequencia)
