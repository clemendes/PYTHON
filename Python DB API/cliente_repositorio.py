import mysql.connector
from fabrica_conexao import FabricaConexao

class ClienteRepositorio():

   @staticmethod
   def listar_clientes():
      db = FabricaConexao.conectar()
      try:
         cursor = db.cursor()
         cursor.execute("SELECT * FROM cliente")
         print(cursor.fetchall())
      finally:
         cursor.close()
         db.close()

   @staticmethod
   def inserir_cliente(cliente):
      db = FabricaConexao.conectar()
      try:
         cursor = db.cursor()
         cursor.execute("INSERT INTO cliente (nome, idade) VALUES (%s,%s)",
                        (cliente.nome, cliente.idade))
      finally:
         cursor.close()
         db.close()

   @staticmethod
   def editar_cliente(id_cliente, cliente):
      db = FabricaConexao.conectar()
      try:
         cursor = db.cursor()
         cursor.execute("UPDATE cliente SET nome=%s, idade=%s WHERE idcliente=%s",
                        (cliente.nome, cliente.idade, id_cliente))
      finally:
         cursor.close()
         db.close()    

   @staticmethod
   def remover_cliente(id_cliente):
      db = FabricaConexao.conectar()
      try:
         cursor = db.cursor()
         cursor.execute("DELETE FROM cliente WHERE idcliente=%s", 
                        (id_cliente,))
      finally:
         cursor.close()
         db.close()