import PySimpleGUI as sg

class TelaRemoveUsuario:

    def __init__(self):
        self.__window = None

    def init_components(self, usuario):
        sg.theme("Reddit")
        layout = [
            [sg.Text("Deseja remover esse usuário?")],
            [sg.Text(f'Nome: {usuario.nome}', size=(10, 1))],
            [sg.Text(f'Nome: {usuario.codigo}', size=(10, 1))],
            [sg.Submit("Remover", key='remover', button_color='gray'),sg.Submit("Cancelar", button_color='red', key='cancelar')]
        ]

        self.__window = sg.Window("Remover usuário", layout=layout, resizable=False, finalize=True)
        self.__window.set_min_size((50, 50))

    def open(self):
        botao, valores = self.__window.Read()

        return botao

    def close(self):
        self.__window.Close()

    def show_message(self, titulo: str, msg):
        sg.Popup(titulo, msg)