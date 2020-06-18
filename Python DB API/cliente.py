class Cliente():
   
   # ----- METODO CONSTRUCTOR ------
   def __init__(self, nome, idade):
      self.__nome = nome   # privado
      self.__idade = idade # privado

   # --------- METODOS GET ---------
   @property
   def nome(self):
      return self.__nome

   @property
   def idade(self):
      return self.__idade

   # --------- METODOS SET ---------
   @nome.setter
   def nome(self, nome):
      self.__nome = nome

   @idade.setter
   def idade(self, idade):
      self.__idade = idade