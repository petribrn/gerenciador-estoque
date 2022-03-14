import PySimpleGUI as sg
from limite.abstract_tela import Tela

class TelaListaEntidades(Tela):

    def __init__(self):
        pass

    def init_components(self, lista_entidades, nome_colunas, nome_tela):

        sg.theme("Reddit")
        layout = [
                    [sg.Table(values=lista_entidades, headings=nome_colunas, max_col_width=35,
                              auto_size_columns=True,
                              display_row_numbers=False,
                              justification='center',
                              num_rows=len(lista_entidades),
                              key='tabela_entidades',
                              row_height=35,
                              tooltip=nome_tela)],
                    [sg.Cancel("Ok", key='ok')]
                ]

        super().__init__(sg.Window(nome_tela, layout=layout, resizable=True, finalize=True, modal=True),(200,(len(lista_entidades)+1)*10) )

    def open(self):
        while True:
            botao, valores = super().read()
            if botao == 'ok' or botao == None or botao == sg.WIN_CLOSED:
                break
        return botao