import PySimpleGUI as sg
from limite.abstract_tela import Tela

class TelaEstoque(Tela):

    def __init__(self):
        pass

    def init_components(self):
        sg.theme("Reddit")
        layout = [
                    [sg.Text("Escolha as opções:")],
                    [sg.Submit("Fazer movimentação", key=1)],
                    [sg.Submit("Listar estoque", key=2)],
                    [sg.Submit("Listar movimentações", key=3)],
                    [sg.Submit("Listar movimentações de um usuário", key=4)],
                    [sg.Cancel("Retornar", key=5, button_color='gray'), sg.Cancel('Sair', key=0, button_color='red')]
                ]

        super().__init__(sg.Window("Tela de movimentações", layout=layout, resizable=True, modal=True, finalize=True), (200,200))

    def open(self):
        botao, valores = super().read()
        if botao == None or botao == sg.WIN_CLOSED or botao == 5:
            super().close()
        return botao
