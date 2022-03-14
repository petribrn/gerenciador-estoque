import PySimpleGUI as sg
from limite.abstract_tela import Tela

class TelaRemoveUsuario(Tela):

    def __init__(self):
        pass

    def init_components(self, usuario):
        sg.theme("Reddit")
        layout = [
            [sg.Text("Deseja remover esse usuário?")],
            [sg.Text(f'Nome: {usuario.nome}', size=(10, 1))],
            [sg.Text(f'Codigo: {usuario.codigo}', size=(10, 1))],
            [sg.Submit("Remover", key='remover', button_color='gray'),sg.Submit("Cancelar", button_color='red', key='cancelar')]
        ]

        super().__init__(sg.Window("Remover usuário", layout=layout, resizable=False, finalize=True), (50,50))

    def open(self):
        botao, valores = super().read()

        return botao