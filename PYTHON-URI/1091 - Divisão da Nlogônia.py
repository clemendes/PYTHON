# URI 1091
# CLEVERSON MENDES FARIA

while (True):
    
    consultas = int(input())
    
    if consultas == 0:
        break
        
    coordenadas = input().split()
        
    for i in range(consultas):
        posicao = input().split()
        
        if (coordenadas[0] == posicao[0]) or (coordenadas[1] == posicao[1]):
            print("divisa")
            
        elif (int(posicao[0]) > int(coordenadas[0])):
            if (int(posicao[1]) > int(coordenadas[1])):
                print("NE")
            else:
                print("SE")
                
        else:
            if (int(posicao[1]) > int(coordenadas[1])):
                print("NO")
            else:
                print("SO")
