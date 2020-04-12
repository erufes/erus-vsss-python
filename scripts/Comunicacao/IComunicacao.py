""" Nome do módulo :        IComunicacao.py
    Ano de criação :        2019/10
    Descrição do módulo :   Interface de Comunicacao
    Versão :                1.0
    Pré-requisitos :        Nenhum
    Membros :               Lorena Bassani
"""


class IComunicacao(object):

    def enviaMensagem(self, Mensagem, Receptor, Remetente=None):
        raise NotImplementedError

    def recebeMensagem(self):
        raise NotImplementedError
