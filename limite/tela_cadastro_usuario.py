import PySimpleGUI as sg
from limite.abstract_tela import Tela
from exceptions.entrada_vazia_exception import EntradaVaziaException
from exceptions.codigo_invalido_exception import CodigoInvalidoException
from exceptions.codigo_ja_cadastrado_exception import CodigoJaCadastradoException
from exceptions.nome_invalido_exception import NomeInvalidoException


class TelaCadastroUsuario(Tela):

    def __init__(self):
        pass

    def init_components(self):

        sg.theme("Reddit")
        layout = [
                    [sg.Text("Incluir novo usuário:")],
                    [sg.Text("Nome:", size=(10,1)), sg.InputText(key='nome', size=(18,1))],
                    [sg.Text("Código:", size=(10,1)), sg.InputText(key='codigo', size=(15,1))],
                    [sg.Submit("Incluir", key='incluir', button_color='gray'), sg.Cancel("Cancelar", button_color='red', key='cancel')]
                ]

        super().__init__(sg.Window("Cadastro de Usuário", layout=layout, resizable=False, finalize=True), (50,50))


    def open(self, lista_entidade):
        while True:
            botao, valores = super().read()
            if botao == 'incluir':
                try:
                    if valores is not None and valores['nome'] != '' and valores['codigo'] != '':
                        try:
                            if not (valores['codigo'] == '' or valores['codigo'] == None):

                                if valores['codigo'].isnumeric() == False:
                                    raise CodigoInvalidoException
                                elif valores['nome'].isascii() == False or valores['nome'].isnumeric() == True:
                                    raise NomeInvalidoException
                                elif len(valores['nome']) < 2 or len(valores['nome']) > 15:
                                    raise NomeInvalidoException

                                else:
                                    valores['codigo'] = int(valores['codigo'])
                                    if valores['codigo'] in lista_entidade:
                                        raise CodigoJaCadastradoException(valores['codigo'])

                                    super().close()
                                    break

                        except CodigoInvalidoException as e:
                            super().show_message('Código inválido!', e)
                        except NomeInvalidoException as n:
                            super().show_message("Nome inválido!", n)
                        except CodigoJaCadastradoException as f:
                            super().show_message('Código já cadastrado!', f)
                    else:
                        raise EntradaVaziaException
                except EntradaVaziaException as g:
                    super().show_message('Campos incompletos!', g)

            elif botao == 'cancel':
                super().close()
                break

            elif botao in ('cancel', sg.WIN_CLOSED):
                super().close()
                break

        return botao, valores