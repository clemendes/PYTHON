# URI 1041
# CLEVERSON MENDES FARIA

entradas = input().split()

x = float(entradas[0])
y = float(entradas[1])

	
if (x>0 and y>0):
    print("Q1")	
elif (x<0 and y>0):
    print("Q2")
elif (x<0 and y<0):
    print("Q3")
elif (x>0 and y<0):
    print("Q4")		    
elif (x==0 and y ==0):
    print("Origem")
elif (y == 0 and x != 0 ):
    print("Eixo X")
elif (x == 0 and y != 0 ):
    print("Eixo Y")
