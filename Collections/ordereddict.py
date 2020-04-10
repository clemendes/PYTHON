
from collections import OrderedDict
import os

os.system("cls")

dicionario_ordenado = OrderedDict()

dicionario_ordenado['a'] = 1
dicionario_ordenado['b'] = 2
dicionario_ordenado['c'] = 3
dicionario_ordenado['d'] = 4
dicionario_ordenado['e'] = 5

print(dicionario_ordenado)

# Resultado: OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])

# EXEMPLO 
class Produto ():
    def __init__(self, nome, preco):
      self.__nome = nome
      self.__preco = preco
    
    def __str__(self):
        return "{!s} - R${:.2f}".format(self.__nome, self.__preco)

if __name__ == "__main__":

    t = int(input())

    produtos = dict()

    for i in range(0, t):
        codigo, nome, preco = input().split()
        produtos.update({ int(codigo): Produto(nome, float(preco))})
    
    estoque = OrderedDict()
    [estoque.update({k:v}) for k, v in sorted(produtos.items(),reverse=True) if k%2 != 0 ]
    [estoque.update({k:v}) for k, v in sorted(produtos.items()) if k%2 == 0 ]
    
    [print("{:d}={!s}".format(k,v)) for k, v in estoque.items()]
    
    # Também poderia ser:
    
    # dicionario_impar = dict()
    # for k in produtos.keys():
    #     if k%2 != 0:
    #         dicionario_impar.update({k: produtos[k]})
            
    # dicionario_par = dict()
    # for k in produtos.keys():
    #     if k%2 == 0:
    #         dicionario_par.update({k: produtos[k]})
    
    # for k,v in sorted(dicionario_impar.items(),reverse=True):
    #     estoque.update({k:v})
        
    
    # for k,v in sorted(dicionario_par.items()):
    #     estoque.update({k:v})
    
    # for k,v in estoque.items():
    #     print("{:d}={!s}".format(k,v))