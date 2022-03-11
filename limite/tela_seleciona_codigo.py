import PySimpleGUI as sg
from limite.abstract_tela import Tela
from exceptions.valor_invalido_exception import ValorInvalidoException
from exceptions.entrada_vazia_exception import EntradaVaziaException


class TelaSelecionaCodigo(Tela):

    def __init__(self):
        pass

    def init_components(self):
        sg.theme("Reddit")
        layout = [
            [sg.Text("Digite o código:")],
            [sg.Text("Código:", size=(10, 1)), sg.InputText(key='codigo', size=(15, 1))],
            [sg.Submit("Buscar", key='buscar', button_color='gray'),sg.Submit("Cancelar", button_color='red', key='cancelar')]
        ]

        super().__init__(sg.Window("Busca por código", layout=layout, resizable=False, finalize=True), (50,50))

    def open(self):
        while True:
            botao, valores = super().read()
            if botao == 'buscar':
                try:
                    if valores is not None and valores['codigo'] != '':
                        try:
                            if not (valores['codigo'] == '' or valores['codigo'] == None):

                                if valores['codigo'].isnumeric() == False:
                                    raise ValorInvalidoException
                                else:
                                    valores['codigo'] = int(valores['codigo'])
                                    super().close()
                                    break

                        except ValorInvalidoException as e:
                            super().show_message('Código inválido!', e)
                    else:
                        raise EntradaVaziaException

                except ValorInvalidoException as f:
                    super().show_message('Valor inválido!', f)

                except EntradaVaziaException as g:
                    super().show_message('Campos incompletos!', g)

            elif botao == 'cancelar':
                super().close()
                break

            elif botao in ('cancelar', sg.WIN_CLOSED):
                super().close()
                break

        return botao, valores['codigo']