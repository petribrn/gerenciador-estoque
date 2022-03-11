import PySimpleGUI as sg
from limite.abstract_tela import Tela

class TelaListaUmUsuario(Tela):

    def __init__(self):
        pass

    def init_components(self, usuario):
        sg.theme("Reddit")
        layout = [
            [sg.Text("Usuário encontrado!")],
            [sg.Text(f'Nome: {usuario.nome}', size=(10, 1))],
            [sg.Text(f'Código: {usuario.codigo}', size=(10, 1))],
            [sg.Submit("Ok", key='ok')]
        ]

        super().__init__(sg.Window("Listar um usuário", layout=layout, resizable=False, finalize=True), (50,50))

    def open(self):
        while True:
            botao, valores = super().read()

            if botao == 'ok' or botao == None or botao == sg.WIN_CLOSED:
                break

        return botao