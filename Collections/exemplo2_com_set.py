import os

os.system("cls")

class Carro():

    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo
        
    @property
    def ano(self):
        return self.__ano

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo
        
    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    def __hash__(self):
        primo = 31
        return primo * hash(self.__marca) + primo * hash(self.__modelo) + primo * hash(self.__ano)

    def __eq__(self, obj):
        if (obj == None):
			      return False
        if (self.__class__ != obj.__class__):
			      return False
        if (self.__marca == None):
            if(obj.marca != None):
                return False
            elif(self.__marca != obj.marca):
                return False
        if (self.__modelo == None):
            if (obj.modelo != None):
                return False
            elif (self.__modelo != obj.modelo):
                return False
        if (self.__ano == None):
            if (obj.ano != None):
                return False
            elif (self.__ano != obj.ano):
                return False
        
        return True

    def __str__(self):
        return self.__marca + " - " + self.__modelo  + " - " + str(self.__ano)
        
if __name__ == "__main__":
         
    t = int(input())

    colecao = set()
    for i in range(0, t):

        marca, modelo, ano = input().split()
      
        colecao.add(Carro(marca, modelo, int(ano)))
    
    
    colecao_ordenada = sorted(colecao, key=str)
    
    for c in colecao_ordenada:
        print(c)