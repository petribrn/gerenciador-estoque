import PySimpleGUI as sg
from exceptions.valor_invalido_exception import ValorInvalidoException
from exceptions.entrada_vazia_exception import EntradaVaziaException

class TelaSelecionaCodigo:

    def __init__(self):
        self.__window = None

    def init_components(self):
        sg.theme("Reddit")
        layout = [
            [sg.Text("Digite o código:")],
            [sg.Text("Código:", size=(10, 1)), sg.InputText(key='codigo', size=(15, 1))],
            [sg.Submit("Buscar", key='buscar', button_color='gray'),sg.Submit("Cancelar", button_color='red', key='cancelar')]
        ]

        self.__window = sg.Window("Busca por código", layout=layout, resizable=False, finalize=True)
        self.__window.set_min_size((50, 50))

    def open(self):
        while True:
            botao, valores = self.__window.Read()
            if botao == 'buscar':
                try:
                    if valores is not None and valores['codigo'] != '':
                        try:
                            if not (valores['codigo'] == '' or valores['codigo'] == None):

                                if valores['codigo'].isnumeric() == False:
                                    raise ValorInvalidoException
                                else:
                                    valores['codigo'] = int(valores['codigo'])
                                    self.close()
                                    break

                        except ValorInvalidoException as e:
                            self.show_message('Código inválido!', e)
                    else:
                        raise EntradaVaziaException

                except ValorInvalidoException as f:
                    self.show_message('Valor inválido!', f)

                except EntradaVaziaException as g:
                    self.show_message('Campos incompletos!', g)

            elif botao == 'cancelar':
                self.close()
                break

            elif botao in ('cancelar', sg.WIN_CLOSED):
                self.close()
                break

        return botao, valores['codigo']

    def close(self):
        self.__window.Close()

    def show_message(self, titulo: str, msg):
        sg.Popup(titulo, msg)