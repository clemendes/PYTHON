# URI 2242
# CLEVERSON MENDES FARIA

# LOGICA UTILIZADA
# DECLARAR UMA STRING COM AS 5 VOGAIS
# GRAVAR A ENTRADA EM UMA STRING SOMENTE SE FOR IGUAL A UMA DAS 05 VOGAIS
# FAZER A COMPARACAO INVERSA

vogais = ('a','e','i','o','u')
entr_vogais = []
a = []
contador = 0

entrada = input()

for i in entrada:
    for j in vogais:
        if i == j:
            entr_vogais.append(i) # GRAVANDO VETOR COM AS VOGAIS DE ENTRADAS

a = entr_vogais[::-1]             # GRAVANDO NOVO VETOR COM INVERSÃO

for i in range(0,len(a),1):       # TESTANDO SE AS VOGAIS DE ENTRADAS SAO
    if a[i] == entr_vogais[i]:    # IGUAIS A INVERSAO DAS MESMAS 
        contador += 1

if contador == len(a):            # SE FOREM IGUAIS EM AMBOS SENTIDOS ENTAO
    print("S")                    # PRINT 'S' SE NAO 'N'
else:
    print("N")
