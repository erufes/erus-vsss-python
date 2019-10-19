""" Nome do módulo :        Singleton
    Ano de criação :        2019/10
    Descrição do módulo :   Módulo que implementa padrão Singleton
    Versão :                2.0
    Pré-requisitos :        Nenhum
    Membros :               Lorena B. Bassani
"""

class Singleton(object):
    __single = None # the one, true Singleton

    def __new__(classtype, *args, **kwargs):
        # Check to see if a __single exists already for this class
        # Compare class types instead of just looking for None so
        # that subclasses will create their own __single objects
        if classtype != type(classtype.__single):
            classtype.__single = object.__new__(classtype)
            classtype.inicializa(classtype.__single, *args, **kwargs)
        return classtype.__single
    
    def inicializa(self, *args, **keyargs):
        raise NotImplementedError

