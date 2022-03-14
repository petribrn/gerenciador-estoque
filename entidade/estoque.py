from entidade.produto import Produto

class Estoque:
  def __init__(self, produto: Produto, quantidade: int):
    if (isinstance(produto, Produto)):
        self.__produto = produto
    self.__quantidade = quantidade

  @property
  def produto(self):
    return self.__produto

  @property
  def quantidade(self):
    return self.__quantidade

  @produto.setter
  def produto(self, produto: Produto):
    if (isinstance(produto, Produto)):
        self.__produto = produto

  @quantidade.setter
  def quantidade(self, quantidade: int):
    self.__quantidade = quantidade
    