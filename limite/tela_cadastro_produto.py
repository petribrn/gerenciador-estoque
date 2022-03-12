import PySimpleGUI as sg
from limite.abstract_tela import Tela
from exceptions.entrada_vazia_exception import EntradaVaziaException
from exceptions.valor_invalido_exception import ValorInvalidoException
from exceptions.codigo_ja_cadastrado_exception import CodigoJaCadastradoException


class TelaCadastroProduto(Tela):

    def __init__(self):
        pass

    def init_components(self):

        sg.theme("Reddit")
        layout = [
                    [sg.Text("Incluir novo produto:")],
                    [sg.Text("Nome:", size=(10,1)), sg.InputText(key='nome', size=(15,1))],
                    [sg.Text("Cor:", size=(10,1)), sg.InputText(key='cor', size=(15,1))],
                    [sg.Text("Tipo:", size=(10, 1)), sg.InputText(key='tipo', size=(15, 1))],
                    [sg.Text("Descrição:", size=(10, 1)), sg.InputText(key='descricao', size=(15, 2))],
                    [sg.Text("Código:", size=(10, 1)), sg.InputText(key='codigo', size=(15, 1))],
                    [sg.Submit("Incluir", key='incluir', button_color='gray'), sg.Cancel("Cancelar", button_color='red', key='cancel')]
                ]

        super().__init__(sg.Window("Cadastro de Produto", layout=layout, resizable=False, finalize=True), (50,50))


    def open(self, lista_entidade):
        while True:
            botao, valores = super().read()
            if botao == 'incluir':
                try:
                    if valores is not None:
                        if valores['nome'] == '':
                            raise EntradaVaziaException
                        elif valores['cor'] == '':
                            raise EntradaVaziaException
                        elif valores['tipo'] == '':
                            raise EntradaVaziaException
                        elif valores['descricao'] == '':
                            raise EntradaVaziaException
                        elif valores['codigo'] == '':
                            raise EntradaVaziaException
                        else:
                            try:
                                if valores['codigo'].isnumeric() == False:
                                    raise ValorInvalidoException
                                elif valores['nome'].isascii() == False or valores['nome'].isnumeric() == True:
                                    raise ValorInvalidoException
                                elif len(valores['nome']) < 2 or len(valores['nome']) > 15:
                                    raise ValorInvalidoException
                                elif valores['cor'].isalpha() == False or valores['tipo'].isalpha() == False:
                                    raise ValorInvalidoException
                                elif len(valores['cor']) < 2 or len(valores['tipo']) < 2:
                                    raise ValorInvalidoException
                                elif valores['descricao'].isascii() == False or valores['descricao'].isnumeric() == True:
                                    raise ValorInvalidoException
                                elif len(valores['descricao']) < 2 or len(valores['descricao']) > 30:
                                    raise ValorInvalidoException
                                else:
                                    valores['codigo'] = int(valores['codigo'])
                                    if valores['codigo'] in lista_entidade:
                                        raise CodigoJaCadastradoException(valores['codigo'])
                                    super().close()
                                    break

                            except ValorInvalidoException as e:
                                super().show_message('Código inválido!', e)
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