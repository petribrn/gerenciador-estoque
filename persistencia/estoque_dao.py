from persistencia.abstract_dao import AbstractDAO
from entidade.estoque import Estoque

class EstoqueDAO(AbstractDAO):

    def __init__(self):
        super().__init__('estoque.pkl')

    def persist(self, estoque: Estoque):
        if self.__estoque_valida(estoque):
            super().persist(estoque, estoque)

    def remove(self, estoque: Estoque):
        if self.__estoque_valida(estoque):
            super().remove(estoque)

    def __estoque_valida(self, estoque):
        return (estoque is not None) and (isinstance(estoque, Estoque))