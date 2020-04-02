# URI 1040
# CLEVERSON MENDES FARIA

notas = input().split()

n1 = float(notas[0])
n2 = float(notas[1])
n3 = float(notas[2])
n4 = float(notas[3])

media = (((n1*2) + (n2*3) + (n3*4) + (n4*1))/10)

print("Media: %.1f" %media)

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 7.0 and media >= 5.0:
    print("Aluno em exame.")

    nf = float(input())

    print("Nota do exame:", nf)

    media2 = float((media + nf) / 2.0)
    
    if media2 >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print("Media final:",media2)
     
else: 
    print("Aluno reprovado.")
