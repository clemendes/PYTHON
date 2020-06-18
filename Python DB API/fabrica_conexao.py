import mysql.connector, os
from configparser import ConfigParser

class FabricaConexao():

   @staticmethod
   def conectar():
      config = ConfigParser()
      config_file = os.path.join(os.path.dirname(__file__), 'config.ini')
      config.read(config_file)
      db = mysql.connector.connect(user=config['DATABASE']['user'],
                                    passwd=config['DATABASE']['passwd'],
                                    db=config['DATABASE']['db'],
                                    host=config['DATABASE']['host'], 
                                    port=int(config['DATABASE']['port']),
                                    autocommit=config['DATABASE']['autocommit'])

      return db