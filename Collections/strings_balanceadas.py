from collections import deque
import re
    
def analisa_fila(fila):
    if(fila != None):
        caractere = fila.popleft()
        parentese = 0
        chave = 0
        colchete = 0
        while(True):
            if (caractere == "("):
              parentese+=1
            elif (caractere == ")"):
                if(parentese==0):
                    return False
                else:
                    parentese-=1
            elif (caractere == "["):
                colchete+=1
            elif (caractere == "]"):
                if(colchete==0):
                    return False
                else:
                    colchete-=1
                break;
            elif (caractere == "{"):
                chave+=1
            elif (caractere == "}"):
                if(chave==0):
                    return False
                else:
                    chave-=1
            else:
                return False

            try:
              caractere = fila.popleft()
            except IndexError:
              break

        if(chave == 0 and parentese == 0 and colchete == 0):
            return True
        else:
          return False
    
    return False


if __name__ == "__main__":
    t = int(input())
    for i in range(0, t):
        fila = deque()
        for c in input():
            fila.append(c)
            
        print("Balanceada" if analisa_fila(fila) else "Não balanceada")

    filtro = {k: type(v) for k, v in vars().copy().items() if not re.search(r'\b__\w+__\b', k) }

    if(not deque in filtro.values()):
        print('É necessário fazer uso da classe deque')

    if(list in filtro.values()) or (tuple in filtro.values()):
        print('Não pode ser utilizado lista ou tupla')