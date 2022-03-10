import PySimpleGUI as sg
from exceptions.entrada_vazia_exception import EntradaVaziaException
from exceptions.valor_invalido_exception import ValorInvalidoException

class TelaAlteraUsuario:

    def __init__(self):
        self.__window = None

    def init_components(self, usuario):

        sg.theme("Reddit")
        layout = [
                    [sg.Text("Alterar usuário:")],
                    [sg.Text(f"Antigo nome: {usuario.nome}")],
                    [sg.Text("Novo nome:", size=(10,1)), sg.InputText(key='novo_nome', size=(18,1))],
                    [sg.Submit("Alterar", key='alterar', button_color='gray'), sg.Cancel("Cancelar", button_color='red', key='cancel')]
                ]

        self.__window = sg.Window("Alteração de Usuário", layout=layout, resizable=False, finalize=True)
        self.__window.set_min_size((50,50))

    def open(self):
        while True:
            botao, valores = self.__window.Read()
            if botao == 'alterar':
                try:
                    if valores is not None and valores['novo_nome'] != '' and valores['novo_nome'] is not None:
                        try:
                            if valores['novo_nome'].isascii() == False or valores['novo_nome'].isnumeric() == True:
                                raise ValorInvalidoException

                            elif len(valores['novo_nome']) < 2 or len(valores['novo_nome']) > 15:
                                raise ValorInvalidoException # criar exception para strings invalidas

                            else:
                                valores['novo_nome'] = valores['novo_nome']
                                self.close()
                                break

                        except ValorInvalidoException as e:
                            self.show_message('Nome inválido!', e)
                    else:
                        raise EntradaVaziaException

                except EntradaVaziaException as f:
                    self.show_message('Campos incompletos!', f)

            elif botao == 'cancel':
                self.close()
                break

            elif botao in ('cancel', sg.WIN_CLOSED):
                self.close()
                break

        return botao, valores['novo_nome']

    def close(self):
        self.__window.Close()

    def show_message(self, titulo: str, msg):
        sg.Popup(titulo, msg)