import mysql.connector
from mysql.connector import Error

""" --------------------------------------
    INICIAR A CONEXÃO COM O BACO DE DADOS 
    -------------------------------------- """
# FORMA SIMPLES SEM A TRATATIVA DE ERROS
mysql.apilevel = "1.0"
db = mysql.connector.connect(user='root', passwd='root', db='treinaweb_clientes', host='127.0.0.1',
                             auth_plugin='mysql_native_password', port=3306, autocommit=False)
print("Conexão realizada com sucesso!")

"""
   try:
      connection = mysql.connector.connect(host='127.0.0.1', 
                                          database='treinaweb_clientes',
                                          user='root', 
                                          password='root',
                                          auth_plugin='mysql_native_password')
      if connection.is_connected():
         db_Info = connection.get_server_info()
         print("Connected to MySQL Server version", db_Info)
         cursor = connection.cursor()
         cursor.execute("select database();")
         record = cursor.fetchone()
         print("You're connected to database: ", record)

   except Error as e:
      print("Error while connecting to MySQL", e)
   finally:
      if (connection.is_connected()):
         cursor.close()
         connection.close()
         print("MySQL connection is closed")
"""

""" --------------------------------------
    DEFININDO UM CURSOR P/ MANIPULAR OS DADOS
    -------------------------------------- """
cursor = db.cursor(buffered=True)

""" --------------------------------------
    EXECUTANDO UMA QUERY
    -------------------------------------- """
cursor.execute("SELECT * FROM cliente")

""" --------------------------------------
    LENDO DADOS VINDOS DAS CONSULTAS 
    -------------------------------------- """
#FETCHALL() - PERCORRER TODOS OS REGISTROS
print(cursor.fetchall())

# FETCHMANY() - PERCORRRER (X) REGISTROS
cursor.execute("SELECT * FROM cliente")
print(cursor.fetchmany(2))

# FETCHONE() - PERCORRER APENAS 1 REGISTRO
cursor.execute("SELECT * FROM cliente WHERE idcliente=1")
print(cursor.fetchone())

""" --------------------------------------
    INSERINDO DADOS NO BANCO DE DADOS 
    -------------------------------------- """
# cursor.execute("INSERT INTO cliente (nome, idade) VALUES ('Fernando',31)")
# cursor.execute("INSERT INTO cliente (nome, idade) VALUES ('Tereza',34)")
# cursor.execute("INSERT INTO cliente (nome, idade) VALUES ('Marcelo',37)")
# cursor.execute("SELECT * FROM cliente")
# print(cursor.fetchall())

""" --------------------------------------
    CAPTURAR ID DO ÚLTIMO REGISTRO INSERIDO
    -------------------------------------- """
print("ÚLTIMO ID INSERIDO: ", cursor.lastrowid)

""" --------------------------------------
    ALTERANDO DADOS COM COMANDO EXECUTE
    -------------------------------------- """
#cursor.execute("UPDATE cliente SET nome='Josefina' WHERE idcliente=2")

""" --------------------------------------
    EXCLUINDO DADOS COM COMANDO EXECUTE
    -------------------------------------- """
#cursor.execute("DELETE FROM cliente WHERE idcliente=2")

""" --------------------------------------
    UTILIZANDO TRANSAÇÕES COM BD NO PYTHON 
    -------------------------------------- """
try:
    db.begin()
    cursor.execute("INSERT INTO cliente (nome, idade) VALUES ('Leonardo', 29)")
    cursor.execute("INSERT INTO cliente (nome, idade) VALUES ('Marcela', 33)")
    db.commit()
    print("Transação Executada!")
except:
    db.rollback()
    print("Erro na Transação!")

cursor.execute("SELECT * FROM cliente")
print(cursor.fetchall())

""" --------------------------------------
    PARAMETRIZAR CONSULTAS - EVITAR SQL INJETCTOR 
    -------------------------------------- """
nome = 'Cleverson'
idade = 29
cursor.execute("INSERT INTO cliente (nome, idade) VALUES (%s, %s)", (nome, idade))
cursor.execute("SELECT * FROM cliente")
print(cursor.fetchall())

""" --------------------------------------
    INSERIR VARIOS REGISTROS - EXECUTEMANY 
    -------------------------------------- """
cursor.executemany("INSERT INTO cliente (nome, idade) VALUES (%s, %s)",
                    (
                     ('Fabio Junior', 31),
                     ('Henrique Junior', 21),
                     ('Leidiane', 26),
                     ('Donizete', 36)
                    ))

cursor.execute("SELECT * FROM cliente")
print(cursor.fetchall())

""" --------------------------------------
    FECHANDO A CONEXÃO COM O BANCO DE DADOS 
    -------------------------------------- """
# FECHANDO CONEXÃO COM BANCO DE DADOS
cursor.close()
db.close()

""" --------------------------------------
    REFATORANDO OS CODIGOS - ORGANIZADO
    -------------------------------------- """
def listar_clientes(self):
    cursor.execute("SELECT * FROM cliente")
    print(cursor.fetchall())

def inserir_cliente(self, cliente):
    cursor.execute("INSERT INTO cliente (nome, idade) VALUES (%s,%s)",
                     cliente.nome, cliente.idade)

def editar_cliente(self, id_cliente, cliente):
    cursor.execute("UPDATE cliente SET nome=%s, idade=%s WHERE idcliente=%s",
                    cliente.nome, cliente.idade, id_cliente)

def remover_cliente(self, id_cliente):
    cursor.execute("DELETE FROM cliente WHERE idcliente=%s",
                    id_cliente)
