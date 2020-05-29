""" Nome do módulo :        Aliado
    Ano de criação :        2019/10
    Descrição do módulo :   Módulo que descreve um jogador aliado em campo
                                Jogadores Aliados podem ser controlados
    Versão :                2.0
    Pré-requisitos :        Jogador
                            Ponto
                            ComportamentoJogadores
                                Factory
                                IComportamento
    Membros :               Lorena Bassani
"""
from Jogador import Jogador
from Geometria import Ponto
from ComportamentosJogadores.Factory import Factory
from ComportamentosJogadores import Comportamentos
from typing import Optional
# from ComportamentosJogadores.IComportamento import IComportamento


class Aliado(Jogador):

    def __init__(self, idj: int, ponto: Ponto = Ponto(0, 0), comportamento: Optional[Comportamentos.COMPORTAMENTOS] = None):
        super().__init__(idj, ponto)
        self.comportamento: Optional[Comportamentos.COMPORTAMENTOS] = comportamento

    """ Nome da função :     comportamento (getter)
        Intenção da função : Retornar qual o comportamento atual do Jogador
        Pré-requisitos :     Nenhum
        Efeitos colaterais : Nenhum
        Parâmetros :         Nenhum
        Retorno :            COMPORTAMENTOS : Constante da Enumeração COMPORTAMENTOS
    """
    @property
    def comportamento(self):
        return self.__comportamentoId

    # Comentários multi block quebram o código abaixo!
    #    Nome da função :     comportamento (setter)
    #    Intenção da função : Modificar o comportamento atual do Jogador
    #    Pré-requisitos :     Nenhum
    #    Efeitos colaterais : Modifica o comportamento atual do Joagdor
    #    Parâmetros :         COMPORTAMENTOS : Constante da Enumeração COMPORTAMENTOS
    #    Retorno :            Nenhum
    @comportamento.setter
    def comportamento(self, comportamento):
        self.__comportamentoId: Comportamentos.COMPORTAMENTOS = comportamento
        self.__comportamento: Comportamentos.COMPORTAMENTOS = Factory.create(comportamento)

    """ Nome da função :     isInimigo
        Intenção da função : Dizer se o Jogador é Inimigo
        Pré-requisitos :     Ser uma subclasse de Joagador
        Efeitos colaterais : Nenhum
        Parâmetros :         Nenhum
        Retorno :            Boolean : Sempre False
    """
    def isInimigo(self) -> bool:
        return False

    def definirObjetivo(self, mundo):
        return self.__comportamento.definirObjetivo(self, mundo)

    def __str__(self):
        return '[Aliado] ' + super().__str__()
