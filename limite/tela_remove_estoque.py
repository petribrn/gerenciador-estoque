import PySimpleGUI as sg
from limite.abstract_tela import Tela

class TelaRemoveEstoque(Tela):

    def __init__(self):
        pass

    def init_components(self):

        sg.theme("Reddit")
        layout = [
                    [sg.Text("Remover estoque:")],
                    [sg.Text("Quantidade:", size=(10,1)), sg.InputText(key='quantidade', size=(15,1))],
                    [sg.Submit("Incluir", key='incluir', button_color='gray'), sg.Cancel("Cancelar", button_color='red', key='cancel')]
                ]

        super().__init__(sg.Window("Cadastro de Estoque", layout=layout, resizable=False, finalize=True), (50,50))


    def open(self):
        botao, valores = super().read()
        if botao == None or botao == sg.WIN_CLOSED or botao == 'cancel':
            super().close()
        return botao, valores
