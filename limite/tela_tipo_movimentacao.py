import PySimpleGUI as sg
from limite.abstract_tela import Tela

class TelaTipoMovimentacao(Tela):

    def __init__(self):
        pass

    def init_components(self):
        sg.theme("Reddit")
        layout = [
                    [sg.Text("Escolha as opções:")],
                    [sg.Submit("Adicionar", key='adicionar')],
                    [sg.Submit("Remover", key='remover')],
                    [sg.Cancel("Retornar", key='retornar', button_color='gray'), sg.Cancel('Sair', key=0, button_color='red')]
                ]

        super().__init__(sg.Window("Tipo de movimentação", layout=layout, resizable=True, modal=True, finalize=True), (200,200))

    def open(self):
        botao, valores = super().read()
        if botao == None or botao == sg.WIN_CLOSED or botao == 'retornar':
            super().close()
        return botao
