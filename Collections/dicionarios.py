import os

os.system("cls")

# Declarando Dicionario 
dict1 = {1: 'João', 2: 'José'}
dict2 = {'nome': 'João', 'sobrenome': 'Silva', 'idade': 50, 'cargo' : 'Analista de Custos'}

# Declarando Dicionario - Método Dict()
dict3 = dict({1: 'João', 2: 'José'})
dict4 = dict({'nome': 'João', 'sobrenome': 'Silva'})

# Acessando elemento do dicionario
print(dict1[2])

# Percorrer todo o Dicionario com FOR -> Retorna as Chaves
for i in dict1:
   print(i)

# FOR diferenciado para Imprimir Chave + Valor do dicionario
for chave, valor in dict1.items():
   print(chave,valor)

# Get() - Retornar elemento pela chave
print(dict1.get(2))
print(dict2.get('cargo'))

# Len() - Tamanho
print("Tamanho do Dicionario: ", len(dict1))

# Pop() - Remover
dict2.pop('idade')
dict2.pop('cargo')
print(dict2)

# Clear() - Limpar Dict
dict3.clear()
print(dict3)

# Keys - Retornar todas as chaves do dicionário
print(dict1.keys())
print(dict2.keys())

# Adicionado Elementos
dict1[3] = 'Marcos'
dict1[4] = 'Pedro'
dict1['ChaveFinal'] = 'X'
print(dict1)

# Update - Adicionando elementos
dict2.update({'Sexo' : 'M'})
print(dict2)
