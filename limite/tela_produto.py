import PySimpleGUI as sg
from limite.abstract_tela import Tela

class TelaProduto(Tela):

    def __init__(self):
        pass

    def init_components(self):
        sg.theme("Reddit")
        layout = [
                    [sg.Text("Escolha as opções:")],
                    [sg.Submit("Adicionar produto", key=1)],
                    [sg.Submit("Alterar produto", key=2)],
                    [sg.Submit("Excluir produto", key=3)],
                    [sg.Submit("Listar um produto", key=4)],
                    [sg.Submit("Listar todos os produtos", key=5)],
                    [sg.Cancel("Retornar", key=6, button_color='gray'), sg.Cancel('Sair', key=0, button_color='red')]
                ]

        super().__init__(sg.Window("Tela de produtos", layout=layout, resizable=True, modal=True, finalize=True), (200,200))

    def open(self):
        botao, valores = super().read()
        if botao == None or botao == sg.WIN_CLOSED or botao == 6:
            super().close()
        return botao
