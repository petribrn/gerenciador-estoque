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
    lista_produtos = self.__controlador_sistema.controlador_produto.produtos
    lista_usuarios = self.__controlador_sistema.controlador_usuario.usuarios

    if len(lista_produtos) < 1:
      self.__tela__estoque.mostra_mensagem("\nNao foi possivel realizar movimentacao: nao existem produtos cadastrados!")
    elif len(lista_usuarios) < 1:
      self.__tela__estoque.mostra_mensagem("\nNao foi possivel realizar movimentacao: nao existem usuarios cadastrados!")
    else:
      dados_movimentacao = self.__tela__estoque.pega_dados_movimentacao(lista_produtos, lista_usuarios)
      print(dados_movimentacao)

      codigo_movimentacao = randint(1, 100000000)
      produto = controlador_produto.pega_produto_por_codigo(dados_movimentacao["codigo_produto"])
      usuario = controlador_usuario.pega_usuario_por_codigo(dados_movimentacao["codigo_usuario"])

      encontrou = False
      if dados_movimentacao["tipo"] == 'adicionar':
        if len(self.__estoque) < 1:
          self.__estoque.append({"produto": produto.nome, "codigo": produto.codigo, "quantidade": dados_movimentacao["quantidade"]})
        else:
          for item in self.__estoque:
            if item["codigo"] == produto.codigo:
              item['quantidade'] += dados_movimentacao["quantidade"]
              encontrou = True

            if encontrou == False:
              self.__estoque.append({"produto": produto.nome, "codigo": produto.codigo, "quantidade": dados_movimentacao["quantidade"]})
      else:
        for item in self.__estoque:
          if item.codigo == produto.codigo and item.quantidade >= dados_movimentacao["quantidade"]:
            item.quantidade -= dados_movimentacao["quantidade"]
          else:
            self.__tela__estoque.mostra_mensagem("\nQuantidade do produto solicitado em falta!")

      movimentacao = Movimentacao(codigo_movimentacao, usuario, produto, dados_movimentacao["quantidade"], dados_movimentacao["tipo"])
      self.__movimentacoes.append(movimentacao)
      self.__tela__estoque.mostra_mensagem("Movimentacao realizada.")


  def lista_movimentacoes(self):
    if len(self.__movimentacoes) == 0:
      self.__tela__estoque.mostra_mensagem("\nSem movimentacoes registradas!")
    else:
      for e in self.__movimentacoes:
        self.__tela__estoque.mostra_movimentacao({"codigo": e.codigo,
                                                  "nome_produto": e.produto.nome,
                                                  "codigo_produto": e.produto.codigo,
                                                  "nome_usuario": e.usuario.nome,
                                                  "codigo_usuario": e.usuario.codigo, "quantidade": e.quantidade})

  def lista_movimentacao_usuario(self):
    if len(self.__controlador_sistema.controlador_usuario.usuarios) < 1:
      self.__tela__estoque.mostra_mensagem("\nNao foi possivel listar: nao existem usuarios cadastrados.")
    else:
      condigo_usuario = self.__tela__estoque.seleciona_usuario()
      movimentacoes_usuario = []

      for e in self.__movimentacoes:
        if e.usuario.codigo == condigo_usuario:
          movimentacoes_usuario.append(e)


      if len(movimentacoes_usuario) == 0:
        self.__tela__estoque.mostra_mensagem("\nSem movimentacoes para esse usuário registradas!")
      else:
        for e in movimentacoes_usuario:
          self.__tela__estoque.mostra_movimentacao({"codigo": e.codigo,
                                                    "titulo_produto": e.produto.titulo,
                                                    "codigo_produto": e.produto.codigo,
                                                    "nome_usuario": e.usuario.nome,
                                                    "codigo_usuario": e.usuario.codigo})

  def lista_estoque(self):
    if len(self.__estoque) == 0:
      self.__tela__estoque.mostra_mensagem("\nSem itens em estoque!")
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
      try:
        lista_opcoes[self.__tela__estoque.tela_opcoes()]()
      except Exception:
        pass
