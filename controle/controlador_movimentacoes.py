from limite.tela_estoque import TelaEstoque
from entidade.movimentacao import Movimentacao
from controle.controlador_produto import ControladorProduto

from random import randint

class ControladorMovimentacoes():

  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__estoque = []
    self.__movimentacoes = []
    self.__tela__estoque = TelaEstoque()

  def pega_movimentacao_por_codigo(self, codigo: int):
    for movimentacao in self.__movimentacoes:
      if(movimentacao.codigo == codigo):
        return movimentacao
    return None

  def adiciona_movimentacao(self):
    controlador_usuario = self.__controlador_sistema.controlador_usuario
    controlador_produto = self.__controlador_sistema.controlador_produto

    dados_movimentacao = self.__tela__estoque.pega_dados_movimentacao()

    codigo = randint(1, 100000000)
    usuario = controlador_usuario.pega_usuario_por_codigo(dados_movimentacao["codigo_usuario"])
    produto = controlador_produto.pega_produto_por_codigo(dados_movimentacao["codigo_produto"])
    quantidade = dados_movimentacao["quantidade"]
    tipo = dados_movimentacao["tipo"]

    encontrou = False

    if tipo == 'adicionar':
      for item in self.__estoque:
        if item.codigo == produto.codigo:
            item.quantidade += quantidade
            encontrou = True

        if encontrou == False:
          self.__estoque.append({produto: produto, quantidade: quantidade})
    else: 
      for item in self.__estoque:
        if item.codigo == produto.codigo and item.quantidade >= quantidade:
          item -= quantidade
        else:
          self.__tela__estoque.mostra_mensagem("Quantidade do produto solicitado em falta!")
          return

    movimentacao = Movimentacao(codigo, usuario, produto, quantidade, tipo)
    self.__movimentacoes.append(movimentacao)

  def lista_movimentacoes(self):
    if len(self.__movimentacoes) == 0:
      self.__tela__estoque.mostra_mensagem("Sem movimentacoes registradas!")
    else:
      for e in self.__movimentacoes:
        self.__tela__estoque.mostra_movimentacao({"codigo": e.codigo,
                                                  "titulo_produto": e.produto.titulo,
                                                  "codigo_produto": e.produto.codigo,
                                                  "nome_usuario": e.usuario.nome,
                                                  "codigo_usuario": e.usuario.codigo})

  def lista_movimentacao_usuario(self):
    condigo_usuario = self.__tela__estoque.seleciona_usuario()
    movimentacoes_usuario = []

    for e in self.__movimentacoes:
      if e.usuario.codigo == condigo_usuario:
        movimentacoes_usuario.append(e)


    if len(movimentacoes_usuario) == 0:
      self.__tela__estoque.mostra_mensagem("Sem movimentacoes para esse usuário registradas!")
    else:
      for e in movimentacoes_usuario:
        self.__tela__estoque.mostra_movimentacao({"codigo": e.codigo,
                                                  "titulo_produto": e.produto.titulo,
                                                  "codigo_produto": e.produto.codigo,
                                                  "nome_usuario": e.usuario.nome,
                                                  "codigo_usuario": e.usuario.codigo})

  def lista_estoque(self):
    if len(self.__estoque) == 0:
      self.__tela__estoque.mostra_mensagem("Sem itens em estoque!")
    else:
      for e in self.__estoque:
        self.__tela__estoque.mostra_produto({"codigo": e.produto.codigo,
                                                  "titulo_produto": e.produto.titulo,
                                                  "quantidade": e.quantidade})

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.adiciona_movimentacao, 2: self.lista_estoque,  3: self.lista_movimentacoes, 4: self.lista_movimentacao_usuario, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela__estoque.tela_opcoes()]()
