from entidade.usuario import Usuario
from entidade.produto import Produto


class Movimentacao:
  def __init__(self, codigo: int, usuario: Usuario, produto: Produto, quantidade: int, tipo: str):
    if (isinstance(produto, Produto)):
        self.__produto = produto
    if (isinstance(usuario, Usuario)):
        self.__usuario = usuario

    self.__codigo = codigo
    self.__quantidade = quantidade
    self.__tipo = tipo

  @property
  def usuario(self):
    return self.__usuario

  @property
  def produto(self):
    return self.__produto

  @property
  def codigo(self):
    return self.__codigo

  @property
  def quantidade(self):
    return self.__quantidade

  @property
  def tipo(self):
    return self.__tipo

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

  @quantidade.setter
  def quantidade(self, quantidade: int):
    self.__quantidade = quantidade

  @tipo.setter
  def tipo(self, tipo: str):
    self.__tipo = tipo