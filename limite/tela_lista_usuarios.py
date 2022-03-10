import PySimpleGUI as sg

class TelaListaUsuarios:

    def __init__(self):
        self.__window = None

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

        self.__window = sg.Window("Lista de usuários", layout=layout, resizable=True, finalize=True, modal=True)
        self.__window.set_min_size((200,(len(lista_usuarios)+1)*10))

    def open(self):
        while True:
            botao, valores = self.__window.Read()
            if botao == 'ok' or botao == None or botao == sg.WIN_CLOSED:
                break
        return botao

    def close(self):
        self.__window.Close()

    def show_message(self, titulo: str, msg):
        sg.Popup(titulo, msg)

    def tela_opcoes(self):
        return self.open()