import PySimpleGUI as sg
from entidade.produto import Produto
from persistencia.produto_dao import ProdutoDAO
from limite.tela_produto import TelaProduto
from limite.tela_cadastro_produto import TelaCadastroProduto
from limite.tela_seleciona_codigo import TelaSelecionaCodigo
from limite.tela_altera_produto import TelaAlteraProduto
from limite.tela_remove_produto import TelaRemoveProduto
from limite.tela_lista_entidades import TelaListaEntidades


class ControladorProduto:

    def __init__(self, controlador_sistema):
        self.__produto_dao = ProdutoDAO()
        self.__tela_produto = TelaProduto()
        self.__controlador_sistema = controlador_sistema
        self.__tela_cadastro = TelaCadastroProduto()
        self.__tela_seleciona_codigo = TelaSelecionaCodigo()
        self.__tela_altera_produto = TelaAlteraProduto()
        self.__tela_remove_produto = TelaRemoveProduto()
        self.__tela_lista_entidades = TelaListaEntidades()

    @property
    def produtos(self):
        return self.__produto_dao.get_all()

    def inclui_produto(self):
        self.__tela_cadastro.init_components()
        while True:
            botao, valores = self.__tela_cadastro.open(self.__produto_dao.get_all_keys())

            if botao == 'incluir':
                if valores is not None:
                    produto = Produto(valores['nome'],valores['cor'], valores['tipo'], valores['descricao'], valores['codigo'])
                    self.__produto_dao.persist(produto)
                    self.__tela_produto.show_message('Produto adicionado!', f'O produto {produto.codigo} - {produto.nome} foi adicionado.')
                    break
            else:
                break

    def altera_produto(self):
        if len(self.__produto_dao.get_all()) < 1:
            self.__tela_produto.show_message("Erro!", "Não existem produtos cadastrados!")
        else:
            self.__tela_seleciona_codigo.init_components()
            botao, codigo = self.__tela_seleciona_codigo.open()

            produto_encontrado = None
            if botao == 'buscar':
                if codigo is not None and codigo in self.__produto_dao.get_all_keys():
                    for produto in self.__produto_dao.get_all():
                        if produto.codigo == codigo:
                            produto_encontrado = produto
                            self.__tela_produto.show_message("Produto encontrado!",
                                                             f"O produto de código {codigo} foi encontrado.")
                            break
                    self.__tela_altera_produto.init_components(produto_encontrado)
                    while True:
                        botao, valores = self.__tela_altera_produto.open()
                        if botao == 'alterar':
                            if valores is not None:
                                produto_encontrado.nome = valores['nome']
                                produto_encontrado.cor = valores['cor']
                                produto_encontrado.tipo = valores['tipo']
                                produto_encontrado.descricao = valores['descricao']

                                self.__produto_dao.persist(produto_encontrado)
                                self.__tela_altera_produto.show_message("Alteração de produto",
                                                                        'Produto alterado com sucesso!')
                                break
                        else:
                            self.__tela_altera_produto.show_message("Alteração de produto", 'Operação cancelada!')
                            break
                else:
                    if botao != 'cancelar':
                        self.__tela_produto.show_message("Erro!", "Codigo Inexistente!")


    def exclui_produto(self):
        if len(self.__produto_dao.get_all()) < 1:
            self.__tela_produto.show_message('Erro!', 'Não existem produtos cadastrados!')
        else:
            self.__tela_seleciona_codigo.init_components()
            botao, codigo = self.__tela_seleciona_codigo.open()

            produto_encontrado = None

            if botao == 'buscar':
                if codigo is not None and codigo in self.__produto_dao.get_all_keys():
                    for produto in self.__produto_dao.get_all():
                        if produto.codigo == codigo:
                            produto_encontrado = produto
                            self.__tela_produto.show_message("Produto encontrado!",
                                                             f"O produto de código {codigo} foi encontrado.")
                            break
                    self.__tela_remove_produto.init_components(produto_encontrado)
                    while True:
                        botao = self.__tela_remove_produto.open()

                        if botao == 'remover':
                            self.__produto_dao.remove(produto_encontrado)
                            self.__tela_remove_produto.show_message('Remover produto', 'Produto removido com sucesso!')
                            self.__tela_remove_produto.close()
                            break

                        elif botao == 'cancelar':
                            self.__tela_remove_produto.show_message('Remover produto', 'Operação cancelada!')
                            self.__tela_remove_produto.close()
                            break

                        elif botao in ('cancelar', sg.WIN_CLOSED):
                            self.__tela_remove_produto.show_message('Remover produto', 'Operação cancelada!')
                            self.__tela_remove_produto.close()
                            break

                else:
                    if botao != 'cancelar':
                        self.__tela_produto.show_message("Erro!", "Codigo Inexistente!")

    def lista_um_produto(self):
        if len(self.__produto_dao.get_all()) < 1:
            self.__tela_produto.show_message('Erro!', 'Não existem produtos cadastrados!')
        else:
            self.__tela_seleciona_codigo.init_components()
            botao, codigo = self.__tela_seleciona_codigo.open()

            produto_encontrado = None
            informacoes_tabela = []
            colunas = ['Código', 'Produto', 'Tipo', 'Cor', 'Descricao']

            if botao == 'buscar':
                if codigo is not None and codigo in self.__produto_dao.get_all_keys():
                    for produto in self.__produto_dao.get_all():
                        if produto.codigo == codigo:
                            produto_encontrado = produto
                            self.__tela_produto.show_message("Produto encontrado!",
                                                             f"O produto de código {codigo} foi encontrado.")
                            break
                    informacoes_tabela.append([produto_encontrado.codigo, produto_encontrado.nome, produto_encontrado.tipo, produto_encontrado.cor, produto_encontrado.descricao])
                    self.__tela_lista_entidades.init_components(informacoes_tabela, colunas, 'Lista um produto')
                    while True:
                        botao = self.__tela_lista_entidades.open()
                        if botao == 'ok' or botao == None:
                            self.__tela_lista_entidades.close()
                            break
                else:
                    if botao != 'cancelar':
                        self.__tela_produto.show_message("Erro!", "Codigo Inexistente!")


    def lista_produtos(self):
        if len(self.__produto_dao.get_all()) < 1:
            self.__tela_produto.show_message('Erro!', 'Não existem produtos cadastrados!')
        else:
            informacoes_tabela = []
            colunas = ['Código', 'Produto', 'Tipo', 'Cor', 'Descricao']

            for produto in self.__produto_dao.get_all():
                informacoes_tabela.append([produto.codigo, produto.nome, produto.tipo, produto.cor, produto.descricao])
            self.__tela_lista_entidades.init_components(informacoes_tabela, colunas, 'Lista de produtos')
            while True:
                botao = self.__tela_lista_entidades.open()

                if botao == 'ok':
                    self.__tela_lista_entidades.close()
                    break
                else:
                    self.__tela_lista_entidades.close()
                    break


    def retornar(self):
        self.__tela_produto.close()

    def sair(self):
        exit(0)

    def abre_tela(self):
        opcoes = {1: self.inclui_produto, 2: self.altera_produto,
                  3: self.exclui_produto, 4: self.lista_um_produto,
                  5: self.lista_produtos, 6: self.retornar, 0: self.sair}

        while True:
            self.__tela_produto.init_components()
            opcao_escolhida = self.__tela_produto.tela_opcoes()
            self.__tela_produto.close()

            if opcao_escolhida == 6 or opcao_escolhida == None or sg.WIN_CLOSED:
                self.__tela_produto.close()
                break
            else:
                opcoes[opcao_escolhida]()