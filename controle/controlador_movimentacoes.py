from entidade.produto import Produto
from entidade.estoque import Estoque
import PySimpleGUI as sg

from limite.tela_estoque import TelaEstoque
from entidade.movimentacao import Movimentacao
from controle.controlador_produto import ControladorProduto
from persistencia.movimentacao_dao import MovimentacaoDAO
from persistencia.estoque_dao import EstoqueDAO
from limite.tela_seleciona_codigo import TelaSelecionaCodigo
from limite.tela_lista_entidades import TelaListaEntidades

from random import randint

class ControladorMovimentacoes():

  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__estoque_dao = EstoqueDAO()
    self.__movimentacoes_dao = MovimentacaoDAO()
    self.__tela__estoque = TelaEstoque()
    self.__tela_seleciona_codigo = TelaSelecionaCodigo()
    self.__tela_lista_entidades = TelaListaEntidades()

  def pega_movimentacao_por_codigo(self, codigo: int):
    for movimentacao in self.__movimentacoes_dao.get_all():
      if(movimentacao.codigo == codigo):
        return movimentacao
    return None

  def adiciona_movimentacao(self):

    controlador_usuario = self.__controlador_sistema.controlador_usuario
    controlador_produto = self.__controlador_sistema.controlador_produto
    lista_produtos = self.__controlador_sistema.controlador_produto.produtos #usar ProdutoDAO ?
    lista_usuarios = self.__controlador_sistema.controlador_usuario.usuarios # usar UsuarioDAO ?

    if len(lista_produtos) < 1:
      self.__tela__estoque.show_message("\nNao foi possivel realizar movimentacao: nao existem produtos cadastrados!")
    elif len(lista_usuarios) < 1:
      self.__tela__estoque.show_message("\nNao foi possivel realizar movimentacao: nao existem usuarios cadastrados!")
    else:
      dados_movimentacao = self.__tela__estoque.pega_dados_movimentacao(lista_produtos, lista_usuarios)
      print(dados_movimentacao)

      codigo_movimentacao = randint(1, 100000000)
      produto = controlador_produto.pega_produto_por_codigo(dados_movimentacao["codigo_produto"])
      usuario = controlador_usuario.pega_usuario_por_codigo(dados_movimentacao["codigo_usuario"])

      encontrou = False
      if dados_movimentacao["tipo"] == 'adicionar':

        if len(self.__estoque_dao.get_all()) < 1:
          self.__estoque_dao.persist({"produto": produto.nome, "codigo": produto.codigo, "quantidade": dados_movimentacao["quantidade"]})
        else:
          for item in self.__estoque_dao.get_all():
            if item["codigo"] == produto.codigo:
              item['quantidade'] += dados_movimentacao["quantidade"]
              encontrou = True

            if encontrou == False:
              self.__estoque_dao.persist({"produto": produto.nome, "codigo": produto.codigo, "quantidade": dados_movimentacao["quantidade"]})
      else:
        for item in self.__estoque_dao.get_all():
          if item.codigo == produto.codigo and item.quantidade >= dados_movimentacao["quantidade"]:
            item.quantidade -= dados_movimentacao["quantidade"]
          else:
            self.__tela__estoque.show_message("Erro!", "Quantidade do produto solicitado em falta!")

      movimentacao = Movimentacao(codigo_movimentacao, usuario, produto, dados_movimentacao["quantidade"], dados_movimentacao["tipo"])
      self.__movimentacoes_dao.persist(movimentacao)
      self.__tela__estoque.show_message("Movimentacao realizada.")


  def lista_movimentacoes(self):
    if len(self.__movimentacoes_dao.get_all()) < 1:
      self.__tela__estoque.show_message("Erro!", "Não existem movimentações registradas!")
    else:
      informacoes_tabela = []
      colunas = ['Código da movimentação', 'Nome do produto', 'Código do produto', 'Nome do usuário', 'Código do usuário', 'Quantidade']

      for movimentacao in self.__movimentacoes_dao.get_all():
        informacoes_tabela.append([movimentacao.codigo, movimentacao.produto.nome, movimentacao.produto.codigo, movimentacao.usuario.nome, movimentacao.usuario.codigo, movimentacao.quantidade])
      self.__tela_lista_entidades.init_components(informacoes_tabela, colunas, 'Lista de movimentações')
      while True:
              botao = self.__tela_lista_entidades.open()

              if botao == 'ok':
                  self.__tela_lista_entidades.close()
                  break
              else:
                  self.__tela_lista_entidades.close()
                  break

  def lista_movimentacao_usuario(self):
    if len(self.__controlador_sistema.controlador_usuario.usuarios) < 1:
      self.__tela__estoque.show_message("Erro!", "Nao foi possivel listar: nao existem usuarios cadastrados.")
    else:
      condigo_usuario = self.__tela__estoque.seleciona_usuario()
      movimentacoes_usuario = []

      for movimentacao in self.__movimentacoes_dao.get_all():
        if movimentacao.usuario.codigo == condigo_usuario:
          movimentacoes_usuario.append(movimentacao)


      if len(movimentacoes_usuario) < 1:
        self.__tela__estoque.show_message("\nSem movimentacoes para esse usuário registradas!")
      else:
        informacoes_tabela = []
        colunas = ['Código da movimentação', 'Nome do produto', 'Código do produto', 'Nome do usuário', 'Código do usuário', 'Quantidade']

        for movimentacao in movimentacoes_usuario:
          informacoes_tabela.append([movimentacao.codigo, movimentacao.produto.nome, movimentacao.produto.codigo, movimentacao.usuario.nome, movimentacao.usuario.codigo, movimentacao.quantidade])
          self.__tela_lista_entidades.init_components(informacoes_tabela, colunas, 'Lista de movimentações do usuário')

  def lista_estoque(self):
    if len(self.__estoque_dao.get_all()) < 1:
      self.__tela__estoque.show_message("\nSem itens em estoque!")
    else:
      informacoes_tabela = []
      colunas = ['Nome do produto', 'Código do produto', 'Quantidade']

      for estoque in self.__estoque_dao.get_all():
        informacoes_tabela.append([estoque.produto.nome, estoque.produto.codigo, estoque.quantidade])
      self.__tela_lista_entidades.init_components(informacoes_tabela, colunas, 'Lista estoque')
      while True:
                botao = self.__tela_lista_entidades.open()

                if botao == 'ok':
                    self.__tela_lista_entidades.close()
                    break
                else:
                    self.__tela_lista_entidades.close()
                    break

  def retornar(self):
    self.__tela__estoque.close()

  def sair(self):
    exit(0)

  def abre_tela(self):
    opcoes = {1: self.adiciona_movimentacao, 2: self.lista_estoque,  3: self.lista_movimentacoes, 4: self.lista_movimentacao_usuario, 5: self.retornar ,0: self.sair}

    while True:
            self.__tela__estoque.init_components()
            opcao_escolhida = self.__tela__estoque.tela_opcoes()
            self.__tela__estoque.close()

            if opcao_escolhida == 5 or opcao_escolhida == None or sg.WIN_CLOSED:
                self.__tela__estoque.close()
                break
            else:
                opcoes[opcao_escolhida]()
