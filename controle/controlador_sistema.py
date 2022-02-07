from limite.tela_sistema import TelaSistema
from controle.controlador_produto import ControladorProduto
from controle.controlador_usuario import ControladorUsuario
from controle.controlador_movimentacoes import ControladorMovimentacoes

class ControladorSistema:

    def __init__(self):
        self.__controlador_usuario = ControladorUsuario(self)
        self.__controlador_produto = ControladorProduto(self)
        self.__controlador_movimentacoes = ControladorMovimentacoes(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_produto(self):
        return self.__controlador_produto

    @property
    def controlador_usuario(self):
        return self.__controlador_usuario

    @property
    def controlador_movimentacoes(self):
        return self.__controlador_movimentacoes

    def inicializa_sistema(self):
        self.abre_tela()

    def tela_usuario(self):
        self.__controlador_usuario.abre_tela()

    def tela_produto(self):
        # Chama o controlador de produto
        self.__controlador_produto.abre_tela()

    def tela_movimentacoes(self):
        self.__controlador_movimentacoes.abre_tela()
        # Chama o controlador de movimentacoes

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.tela_usuario, 2: self.tela_produto, 3: self.tela_movimentacoes,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
