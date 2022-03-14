from limite.tela_remove_estoque import TelaRemoveEstoque
import PySimpleGUI as sg
from random import randint

from limite.tela_estoque import TelaEstoque
from entidade.movimentacao import Movimentacao
from persistencia.movimentacao_dao import MovimentacaoDAO
from persistencia.estoque_dao import EstoqueDAO
from limite.tela_seleciona_codigo import TelaSelecionaCodigo
from limite.tela_lista_entidades import TelaListaEntidades
from limite.tela_adiciona_estoque import TelaAdicionaEstoque
from persistencia.usuario_dao import UsuarioDAO
from persistencia.produto_dao import ProdutoDAO
from limite.tela_tipo_movimentacao import TelaTipoMovimentacao
from entidade.estoque import Estoque


class ControladorMovimentacoes():

  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__estoque_dao = EstoqueDAO()
    self.__produto_dao = ProdutoDAO()
    self.__usuario_dao = UsuarioDAO()
    self.__movimentacoes_dao = MovimentacaoDAO()
    self.__tela__estoque = TelaEstoque()
    self.__tela_seleciona_codigo = TelaSelecionaCodigo()
    self.__tela_lista_entidades = TelaListaEntidades()
    self.__tela_tipo_movimentacao = TelaTipoMovimentacao()
    self.__tela_adiciona_estoque = TelaAdicionaEstoque()
    self.__tela_remove_estoque = TelaRemoveEstoque()
    self.__estoque = Estoque


  def pega_movimentacao_por_codigo(self, codigo: int):
    for movimentacao in self.__movimentacoes_dao.get_all():
      if(movimentacao.codigo == codigo):
        return movimentacao
    return None

  def adiciona_movimentacao(self):
    if len(self.__produto_dao.get_all()) < 1:
      self.__tela__estoque.show_message("Erro!", "Nao foi possivel realizar movimentacao: nao existem produtos cadastrados!")
    elif len(self.__usuario_dao.get_all()) < 1:
      self.__tela__estoque.show_message("Erro!", "Nao foi possivel realizar movimentacao: nao existem usuarios cadastrados!")
    else:
      self.__tela_tipo_movimentacao.init_components()
      botao = self.__tela_tipo_movimentacao.open()

      encontrou = False
      if botao == 'adicionar':
        self.__tela_seleciona_codigo.init_components()
        while True:
            botao, codigo = self.__tela_seleciona_codigo.open()
            if botao == 'buscar':
                if codigo is not None:
                  for produto in self.__produto_dao.get_all():
                    if codigo == produto.codigo:
                      self.__tela_adiciona_estoque.init_components()
                    break
                  while True:
                    botao, valores_add = self.__tela_adiciona_estoque.open()
                    estoque = Estoque(produto, valores_add['quantidade'])
                    self.__estoque_dao.persist(estoque)
                    self.__tela__estoque.show_message('Estoque adicionado!', 'O produto foi adicionado ao estoque.')
                    break
            else:
                break

      if botao == 'remover':
        self.__tela_seleciona_codigo.init_components()
        while True:
          botao, codigo = self.__tela_seleciona_codigo.open()
          if botao == 'buscar':
                if codigo is not None:
                  for produto in self.__produto_dao.get_all():
                    if codigo == produto.codigo:
                      self.__tela_remove_estoque.init_components()
                    break
                  while True:
                    botao, valores_add = self.__tela_remove_estoque.open()
                    estoque = Estoque(produto, (-valores_add['quantidade']))
                    self.__estoque_dao.persist(estoque)
                    self.__tela__estoque.show_message('Estoque removido!', 'O produto foi removido ao estoque.')

      # else:
      #   for item in self.__estoque_dao.get_all():
      #     if item.codigo == produto.codigo and item.quantidade >= dados_movimentacao["quantidade"]:
      #       item.quantidade -= dados_movimentacao["quantidade"]
      #     else:
      #       self.__tela__estoque.show_message("Erro!", "Quantidade do produto solicitado em falta!")

      # movimentacao = Movimentacao(codigo_movimentacao, usuario, produto, dados_movimentacao["quantidade"], dados_movimentacao["tipo"])
      # self.__movimentacoes_dao.persist(movimentacao)
      # self.__tela__estoque.show_message("Movimentacao realizada.")


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

  def lista_movimentacoes_usuario(self):
    if len(self.__movimentacoes_dao.get_all()) < 1:
      self.__tela__estoque.show_message("Erro!", "Não existem movimentações registradas!")
    if len(self.__controlador_sistema.controlador_usuario.usuarios) < 1:
      self.__tela__estoque.show_message("Erro!", "Nao foi possivel listar: nao existem usuarios cadastrados.")
    else:
      condigo_usuario = self.__tela__estoque.seleciona_usuario()
      movimentacoes_usuario = []

      for movimentacao in self.__movimentacoes_dao.get_all():
        if movimentacao.usuario.codigo == condigo_usuario:
          movimentacoes_usuario.append(movimentacao)


      if len(movimentacoes_usuario) < 1:
        self.__tela__estoque.show_message("Erro!", "Sem movimentacoes para esse usuário registradas!")
      else:
        informacoes_tabela = []
        colunas = ['Código da movimentação', 'Nome do produto', 'Código do produto', 'Nome do usuário', 'Código do usuário', 'Quantidade']

        for movimentacao in movimentacoes_usuario:
          informacoes_tabela.append([movimentacao.codigo, movimentacao.produto.nome, movimentacao.produto.codigo, movimentacao.usuario.nome, movimentacao.usuario.codigo, movimentacao.quantidade])
          self.__tela_lista_entidades.init_components(informacoes_tabela, colunas, 'Lista de movimentações do usuário')

  def lista_estoque(self):
    if len(self.__estoque_dao.get_all()) < 1:
      self.__tela__estoque.show_message("Erro!", "Sem itens em estoque!")
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
    opcoes = {1: self.adiciona_movimentacao, 2: self.lista_estoque,  3: self.lista_movimentacoes, 4: self.lista_movimentacoes_usuario, 5: self.retornar ,0: self.sair}

    while True:
            self.__tela__estoque.init_components()
            opcao_escolhida = self.__tela__estoque.tela_opcoes()
            self.__tela__estoque.close()

            if opcao_escolhida == 5 or opcao_escolhida == None or sg.WIN_CLOSED:
                self.__tela__estoque.close()
                break
            else:
                opcoes[opcao_escolhida]()
