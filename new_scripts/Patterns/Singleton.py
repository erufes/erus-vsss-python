""" Nome do módulo :        Singleton
    Ano de criação :        2019/10
    Descrição do módulo :   Módulo que implementa padrão Singleton
    Versão :                1.0
    Pré-requisitos :        Nenhum
    Membros :               Lorena B. Bassani
"""

class SingletonException(Exception):
    pass

class Singleton(object):
   __instance = None

   """ Nome da função :      getInstance
        Intenção da função : Retornar a instância da classe
        Pré-requisitos :     Nenhum
        Efeitos colaterais : Nova instância pode ser criada se ainda não houver uma
        Parâmetros :         Nenhum
        Retorno :            Singleton : Instância do Singleton
    """
   @staticmethod 
   def getInstance():
      """ Static access method. """
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance
   def __init__(self):
      """ Virtually private constructor. """
      if Singleton.__instance != None:
         raise SingletonException
      else:
         Singleton.__instance = self