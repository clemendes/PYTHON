import copy
import os

os.system("cls")

nested_list = [[1,2,True], ["Olá", "Mundo"]] # LISTAS ENCADEADAS

#---------------------------------------
# * COPIANDO LISTAS - TIPOS DE CÓPIAS **
#---------------------------------------

# Deep Copy - Copia do objeto list
nova_lista = copy.deepcopy(nested_list)
nested_list[0][1] = 'A'
print(nova_lista) 
print(nested_list)

# Shallow Copy - Copia o Endereço de Memória(Referencia)
outra_lista = copy.copy(nested_list)
nested_list[0][1] = 'B'
print(nested_list)
print(outra_lista)




