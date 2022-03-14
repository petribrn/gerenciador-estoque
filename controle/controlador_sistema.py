import PySimpleGUI as sg

from limite.tela_sistema import TelaSistema
from controle.controlador_produto import ControladorProduto
from controle.controlador_usuario import ControladorUsuario
from controle.controlador_movimentacoes import ControladorMovimentacoes

class ControladorSistema:
    __instance = None

    def __init__(self):
        self.__controlador_usuario = ControladorUsuario(self)
        self.__controlador_produto = ControladorProduto(self)
        self.__controlador_movimentacoes = ControladorMovimentacoes(self)
        self.__tela_sistema = TelaSistema()
    
    def __new__(cls):
        if ControladorSistema.__instance is None:
            ControladorSistema.__instance = object.__new__(cls)
        return ControladorSistema.__instance

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
        self.__controlador_produto.abre_tela()

    def tela_movimentacoes(self):
        self.__controlador_movimentacoes.abre_tela()

    def retornar(self):
        self.__tela_sistema.close()

    def sair(self):
        exit(0)

    def abre_tela(self):
        opcoes = {1: self.tela_usuario, 2: self.tela_produto, 3: self.tela_movimentacoes,
                        4: self.retornar, 0: self.sair}

        while True:
            self.__tela_sistema.init_components()
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            self.__tela_sistema.close()

            if opcao_escolhida == 5 or opcao_escolhida == None or sg.WIN_CLOSED:
                self.__tela_sistema.close()
                break
            else:
                opcoes[opcao_escolhida]()
