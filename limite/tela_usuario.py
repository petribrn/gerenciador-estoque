import PySimpleGUI as sg

class TelaUsuario:

    def __init__(self):
        self.__window = None

    def init_components(self):

        sg.theme("Reddit")
        layout = [
                    [sg.Text("Escolha as opções:")],
                    [sg.Submit("Incluir usuário", key=1)],
                    [sg.Submit("Alterar usuário", key=2)],
                    [sg.Submit("Excluir usuário", key=3)],
                    [sg.Submit("Listar um usuário", key=4)],
                    [sg.Submit("Listar todos os usuários", key=5)],
                    [sg.Cancel("Retornar", key=6, button_color='gray'), sg.Cancel('Sair', key=0, button_color='red')]
                ]

        self.__window = sg.Window("Tela de usuários", layout=layout, resizable=True, finalize=True)
        self.__window.set_min_size((200,200))

    def open(self):
        botao, valores = self.__window.Read()
        if botao == None or botao == sg.WIN_CLOSED or botao == 6:
            self.close()
        return botao

    def close(self):
        self.__window.Close()

    def show_message(self, titulo: str, msg):
        sg.Popup(titulo, msg)

    def tela_opcoes(self):
        return self.open()