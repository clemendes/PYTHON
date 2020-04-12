from contato import Contato

# Definições
# arquivo -> as -> namespace para o arquivo
# dados -> Vetor preenchido pela iteração (a cada linha)
# lista_contatos_arquivo -> Dados brutos do arquivo (todas linhas)
# lista_contatos -> Lista de contatos após ajustes strings (retorno)

# Retorna em forma de lista todas as linhas arquivo (contatos)
def listar_contatos():
   lista_contatos = list()
   try:
      with open("contatos.txt", "r") as arquivo:
         lista_contatos_arquivo = arquivo.readlines()
         for i in lista_contatos_arquivo:
            dados = i.split("\t")
            contato_arquivo = Contato(dados[0], dados[1], dados[2])
            lista_contatos.append(contato_arquivo)
      return lista_contatos
   except FileNotFoundError:
      print("Arquivo não encontrado!")

# Insere um novo contato no arquivo (nova linha)
def cadastrar_contato(contato_novo):
   try:
      if buscar_dados_contato(contato_novo.email):
         return False
      else:
         with open("contatos.txt", "a") as arquivo:
            arquivo.write(f"{contato_novo.nome}\t{contato_novo.email}\t{contato_novo.telefone}\n") 
         return True
   except FileNotFoundError:
      print("Arquivo não encontrado!")

# Busca um contato através do e-mail, retornando o índice (linha) 
def buscar_indice_contato(email_contato):
   try:
      with open("contatos.txt", "r") as arquivo:
         lista_contatos = arquivo.readlines()
         for i, linha in enumerate(lista_contatos):
            dados = linha.split("\t")
            if dados[1] == email_contato:
               return i # ENCONTRADO
         else:
            return -1 # NÃO ENCONTRADO
   except FileNotFoundError:
      print("Arquivo não encontrado!")

# Busca os dados do contato, através do email 
def buscar_dados_contato(email_contato):
   try:
      indice = buscar_indice_contato(email_contato)
      if indice>=0: # CONTATO ENCONTRADO
         with open("contatos.txt", "r") as arquivo:
            lista_contatos = arquivo.readlines()
            dados = lista_contatos[indice].split("\t")
            retorno_busca = Contato(dados[0], dados[1], dados[2]) # OBJETO
            return retorno_busca
   except FileNotFoundError:
      print("Arquivo não encontrado!")

# Remove um contato (linha) do arquivo, através do email informado
def remover_contato(email_contato):
   try:
      indice = buscar_indice_contato(email_contato)
      if indice>=0: # CONTATO ENCONTRADO
         with open("contatos.txt", "r") as arquivo:
            lista_contatos = arquivo.readlines()
            contatos = list()
            for i, linha in enumerate(lista_contatos):
               if i != indice: # DIFERENTE DO CONTATO A EXCUIR
                  contatos.append(linha)
         with open("contatos.txt", "w") as arquivo:
            arquivo.writelines(contatos)
         return True 
      else:
         return False
   except FileNotFoundError:
      print("Arquivo não encontrado!")
