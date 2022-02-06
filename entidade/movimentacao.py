from entidade.usuario import Usuario
from entidade.produto import Produto


class Movimentacao:
  def __init__(self, usuario: Usuario, produto: Produto, codigo: int):
    if (isinstance(produto, Produto)):
        self.__produto = produto
    if (isinstance(usuario, Usuario)):
        self.__usuario = usuario

    self.__codigo = codigo

  @property
  def usuario(self):
    return self.__usuario

  @property
  def produto(self):
    return self.__produto

  @property
  def codigo(self):
    return self.__codigo

  @usuario.setter
  def usuario(self, usuario: Usuario):
    if (isinstance(usuario, Usuario)):
        self.__usuario = usuario

  @produto.setter
  def produto(self, produto: Produto):
    if (isinstance(produto, Produto)):
        self.__produto = produto

  @codigo.setter
  def codigo(self, codigo: int):
    self.__codigo = codigo
