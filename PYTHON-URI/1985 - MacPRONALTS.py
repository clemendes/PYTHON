# URI 1985
# CLEVERSON MENDES FARIA

qtd = int(input())
soma = 0;
if (qtd >=1) and (qtd<=5):
    
    for i in range(0,qtd,1):

        leitura = input().split()
        item = str(leitura[0])
        qtd = int(leitura[1])
        
        if (qtd >=1) and (qtd<=500):
            if (item == "1001"):
                soma += qtd*1.50
                
            if (item == "1002"):
                soma += qtd*2.50
                
            if (item == "1003"):
                soma += qtd*3.50
                
            if (item == "1004"):
                soma += qtd*4.50
                
            if (item == "1005"):
                soma += qtd*5.50

print("%.2f" %soma)
