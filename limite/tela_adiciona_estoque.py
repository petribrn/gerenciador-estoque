import PySimpleGUI as sg
from limite.abstract_tela import Tela

from exceptions.entrada_vazia_exception import EntradaVaziaException
from exceptions.codigo_invalido_exception import CodigoInvalidoException
from exceptions.codigo_ja_cadastrado_exception import CodigoJaCadastradoException
from exceptions.nome_invalido_exception import NomeInvalidoException
from exceptions.cor_invalida_exception import CorInvalidaException
from exceptions.tipo_invalido_exception import TipoInvalidoException
from exceptions.descricao_invalida_exception import DescricaoInvalidaException

class TelaAdicionaEstoque(Tela):

    def __init__(self):
        pass

    def init_components(self):

        sg.theme("Reddit")
        layout = [
                    [sg.Text("Adicionar estoque:")],
                    [sg.Text("Quantidade:", size=(10,1)), sg.InputText(key='quantidade', size=(15,1))],
                    [sg.Submit("Incluir", key='incluir', button_color='gray'), sg.Cancel("Cancelar", button_color='red', key='cancel')]
                ]

        super().__init__(sg.Window("Cadastro de Estoque", layout=layout, resizable=False, finalize=True), (50,50))


    def open(self):
        while True:
            botao, valores = super().read()
            if botao == 'incluir':
                try:
                    if valores is not None:
                        if valores['quantidade'] == '':
                            raise EntradaVaziaException
                        else:
                            try:
                                if valores['quantidade'].isnumeric() == False:
                                    raise CodigoInvalidoException
                                else:
                                    valores['quantidade'] = int(valores['quantidade'])
                                    super().close()
                                    break

                            except CodigoInvalidoException as e:
                                super().show_message('Quantidade inválida!', e)
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
