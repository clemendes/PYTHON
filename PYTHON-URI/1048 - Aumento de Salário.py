# URI 1048
# CLEVERSON MENDES FARIA

# 0 - 400.00        15%
# 400.01 - 800.00   12%
# 800.01 - 1200.00  10%
# 1200.01 - 2000.00 7%
# Acima 2000.00     4%

salario = float(input())

if (salario >= 0.00) and (salario <= 400.00):
    novosalario = salario + (salario * 0.15)
    reajuste = salario * 0.15
    percentual = "15 %"
    
    print("Novo salario: %.2f" %novosalario)
    print("Reajuste ganho: %.2f" %reajuste)
    print("Em percentual: %s" %percentual)
    
elif (salario >= 400.01) and (salario <= 800.00):
    novosalario = salario + (salario * 0.12)
    reajuste = salario * 0.12
    percentual = "12 %"
    
    print("Novo salario: %.2f" %novosalario)
    print("Reajuste ganho: %.2f" %reajuste)
    print("Em percentual: %s" %percentual)
    
elif (salario >= 800.01) and (salario <= 1200.00):
    novosalario = salario + (salario * 0.10)
    reajuste = salario * 0.10
    percentual = "10 %"
    
    print("Novo salario: %.2f" %novosalario)
    print("Reajuste ganho: %.2f" %reajuste)
    print("Em percentual: %s" %percentual)
    
elif (salario >= 1200.01) and (salario <= 2000.00):
    novosalario = salario + (salario * 0.07)
    reajuste = salario * 0.07
    percentual = "7 %"
    
    print("Novo salario: %.2f" %novosalario)
    print("Reajuste ganho: %.2f" %reajuste)
    print("Em percentual: %s" %percentual)
    
elif (salario > 2000.00):
    novosalario = salario + (salario * 0.04)
    reajuste = salario * 0.04
    percentual = "4 %"
    
    print("Novo salario: %.2f" %novosalario)
    print("Reajuste ganho: %.2f" %reajuste)
    print("Em percentual: %s" %percentual)
