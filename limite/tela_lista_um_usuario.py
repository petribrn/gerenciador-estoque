import PySimpleGUI as sg

class TelaListaUmUsuario:

    def __init__(self):
        self.__window = None

    def init_components(self, usuario):
        sg.theme("Reddit")
        layout = [
            [sg.Text("Usuário encontrado!")],
            [sg.Text(f'Nome: {usuario.nome}', size=(10, 1))],
            [sg.Text(f'Código: {usuario.codigo}', size=(10, 1))],
            [sg.Submit("Ok", key='ok')]
        ]

        self.__window = sg.Window("Listar um usuário", layout=layout, resizable=False, finalize=True)
        self.__window.set_min_size((50, 50))

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