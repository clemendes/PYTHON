# URI 1173
# CLEVERSON MENDES FARIA

n = int(input())
anterior = 0
vetor = [0,0,0,0,0,0,0,0,0,0]

if (n<=50):
    for i in range(0,10,1):
        if (i == 0):
            vetor[i] = n
            anterior = vetor[i]
            print("N[" + str(i) + "] = " + str(n))
        else:
            vetor[i] = anterior * 2
            anterior = vetor[i]
            print("N[" + str(i) + "] = " + str(vetor[i]))
