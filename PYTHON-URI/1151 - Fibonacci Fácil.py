# URI 1151
# CLEVERSON MENDES FARIA

n = int(input())

seqi = []
seqf = []

for i in range(0,n,1):
 seqi.append(i)
 if (i > 1):
   seqf.append(seqf[i-1]+seqf[i-2])
 else:
   seqf.append(i)

#print(seqi)
#print(seqf)

print(*seqf, sep=" ")
