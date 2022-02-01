from entidade import movimentacao
from limite.tela_estoque import TelaEstoque
from entidade.movimentacao import Movimentacao

from random import randint


# Fazer lançamento e tratamento de exceções, ao invés de apenas mostrar mensagem na tela.
class ControladorMovimentacoes():

  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__movimentacoes = []
    self.__tela__estoque = TelaEstoque()

  def pega_movimentacao_por_codigo(self, codigo: int):
    for movimentacao in self.__movimentacoes:
      if(movimentacao.codigo == codigo):
        return movimentacao
    return None

  #Sugestao: listar apenas os produtos que não estão emprestados
  def incluir_movimentacao(self):
    self.__controlador_sistema.controlador_ususario.lista_ususario()
    self.__controlador_sistema.controlador_produtos.lista_produto()
    dados_movimentacao = self.__tela__estoque.pega_dados_produto()

    usuario = self.__controlador_sistema.controlador_ususario.pega_usuario_por_codigo(dados_movimentacao["codigo"])
    produto = self.__controlador_sistema.controlador_produtos.pega_produto_por_codigo(dados_movimentacao["codigo"])
    movimentacao = Movimentacao(usuario, produto, randint(0, 100))
    self.__movimentacoes.append(movimentacao)

  #Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_movimentacao(self):
    for e in self.__movimentacoes:
      self.__tela__estoque.mostra_movimentacao({"codigo": e.codigo,
                                                "titulo_produto": e.produto.titulo,
                                                "codigo_produto": e.produto.codigo,
                                                "nome_usuario": e.usuario.nome,
                                                "codigo_usuario": e.usuario.codigo})

  def excluir_movimentacao(self):
    self.lista_movimentacao()
    codigo_movimentacao = self.__tela__estoque.seleciona_movimentacao()
    movimentacao = self.pega_movimentacao_por_codigo(int(codigo_movimentacao))

    if (movimentacao is not None):
      self.__movimentacoes.remove(movimentacao)
      self.lista_movimentacao()
    else:
      self.__tela__estoque.mostra_mensagem("ATENÇÃO: Movimentação não existente!")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_movimentacao, 2: self.lista_movimentacao, 3: self.excluir_movimentacao,0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela__estoque.tela_opcoes()]()
