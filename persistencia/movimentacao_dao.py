from persistencia.abstract_dao import AbstractDAO
from entidade.movimentacao import Movimentacao

class MovimentacaoDAO(AbstractDAO):

    def __init__(self):
        super().__init__('movimentacao.pkl')

    def persist(self, movimentacao: Movimentacao):
        if self.__movimentacao_valida(movimentacao):
            super().persist(movimentacao.codigo, movimentacao)

    def remove(self, movimentacao: Movimentacao):
        if self.__movimentacao_valida(movimentacao):
            super().remove(movimentacao.codigo)

    def __movimentacao_valida(self, movimentacao):
        return (movimentacao is not None) and (isinstance(movimentacao, Movimentacao)) and (isinstance(movimentacao.codigo, int))