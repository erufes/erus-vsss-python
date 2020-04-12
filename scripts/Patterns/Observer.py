""" Nome do módulo :        Observer
    Ano de criação :        2019/10
    Descrição do módulo :   Interface do Padrão Observer
    Versão :                1.0
    Pré-requisitos :        Nenhum
    Membros :               Lorena B Bassani
"""


class Observer(object):

    """ Nome da função :        update
        Intenção da função :    Informar a ocorrencia do evento para o observador
        Pré-requisitos :        Desconhecido
        Efeitos colaterais :    Desconhecido
        Parâmetros :            Desconhecido
        Retorno :               Desconhecido
    """

    def update(self, *args, **keyargs):
        raise NotImplementedError


class Notifier(object):
    def __init__(self):
        self.__observers = list()

    """ Nome da função :        attach
        Intenção da função :    Inserir um observador na lista de observação
        Pré-requisitos :        Nenhum
        Efeitos colaterais :    O Observador é inserido na lista de observação
        Parâmetros :            Observer : Observador a ser inserido
        Retorno :               Nenhum
    """

    def attach(self, observer: Observer):
        self.__observers.append(observer)

    """ Nome da função :        dettach
        Intenção da função :    Retirar um Observador da lista de observação
        Pré-requisitos :        Observador estar na lista de observadores
        Efeitos colaterais :    Observador é retirado da lista de observadores
        Parâmetros :            Obervador : Observador a ser retirado da lista de observadores
        Retorno :               Nenhum
    """

    def dettach(self, observer: Observer):
        self.__observers.remove(observer)

    """ Nome da função :        notify
        Intenção da função :    Notificar todos os observadores
        Pré-requisitos :        Nenhum
        Efeitos colaterais :    Todos os obervadores são notificados
        Parâmetros :            Desconhecido
        Retorno :               Nenhum
    """

    def notify(self, *args, **keyargs):
        map(lambda x: x.update(*args, **keyargs), self.__observers)
