import PySimpleGUI as sg
from limite.abstract_tela import Tela

class TelaRemoveProduto(Tela):

    def __init__(self):
        pass

    def init_components(self, produto):
        sg.theme("Reddit")
        layout = [
            [sg.Text("Deseja remover esse produto?")],
            [sg.Text(f"Nome: {produto.nome}", size=(15, 1))],
            [sg.Text(f"Cor: {produto.nome}", size=(15, 1))],
            [sg.Text(f"Tipo: {produto.nome}", size=(15, 1))],
            [sg.Text(f"Descrição: {produto.nome}", size=(15, 1))],
            [sg.Text(f'Codigo: {produto.codigo}', size=(15, 1))],
            [sg.Submit("Remover", key='remover', button_color='gray'), sg.Submit("Cancelar", button_color='red', key='cancelar')]
        ]

        super().__init__(sg.Window("Remover produto", layout=layout, resizable=False, finalize=True), (50,50))

    def open(self):
        botao, valores = super().read()

        return botao