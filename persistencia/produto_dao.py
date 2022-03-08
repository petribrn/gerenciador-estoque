from persistencia.abstract_dao import AbstractDAO
from entidade.produto import Produto

class ProdutoDAO(AbstractDAO):

    def __init__(self):
        super().__init__('produto.pkl')

    def persist(self, produto: Produto):
        if self.__produto_valido(produto):
            super().persist(produto.codigo, produto)

    def remove(self, produto: Produto):
        if self.__produto_valido(produto):
            super().remove(produto.codigo)

    def __produto_valido(self, produto):
        return (produto is not None) and (isinstance(produto, Produto)) and (isinstance(produto.codigo, int))