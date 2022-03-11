import PySimpleGUI as sg
from limite.abstract_tela import Tela

class TelaListaUsuarios(Tela):

    def __init__(self):
        pass

    def init_components(self, lista_usuarios, nome_colunas):

        sg.theme("Reddit")
        layout = [
                    [sg.Table(values=lista_usuarios, headings=nome_colunas, max_col_width=35,
                              auto_size_columns=True,
                              display_row_numbers=False,
                              justification='center',
                              num_rows=len(lista_usuarios),
                              key='tabela_usuarios',
                              row_height=35,
                              tooltip='Lista de usuários')],
                    [sg.Cancel("Ok", key='ok')]
                ]

        super().__init__(sg.Window("Lista de usuários", layout=layout, resizable=True, finalize=True, modal=True),(200,(len(lista_usuarios)+1)*10) )

    def open(self):
        while True:
            botao, valores = super().read()
            if botao == 'ok' or botao == None or botao == sg.WIN_CLOSED:
                break
        return botao