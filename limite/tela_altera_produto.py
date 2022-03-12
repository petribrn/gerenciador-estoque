import PySimpleGUI as sg
from limite.abstract_tela import Tela
from exceptions.entrada_vazia_exception import EntradaVaziaException
from exceptions.valor_invalido_exception import ValorInvalidoException
from exceptions.codigo_ja_cadastrado_exception import CodigoJaCadastradoException


class TelaAlteraProduto(Tela):

    def __init__(self):
        pass

    def init_components(self, produto):

        sg.theme("Reddit")
        layout = [
                    [sg.Text(f"Alterar produto de código {produto.codigo}:")],
                    [sg.Text(f"Nome: {produto.nome}", size=(15,1))],
                    [sg.Text(f"Cor: {produto.cor}", size=(15,1))],
                    [sg.Text(f"Tipo: {produto.tipo}", size=(15,1))],
                    [sg.Text(f"Descrição: {produto.descricao}", size=(15,2))],
                    [sg.Text("Novos dados do produto:")],
                    [sg.Text("Nome:", size=(10,1)), sg.InputText(key='nome', size=(15,1))],
                    [sg.Text("Cor:", size=(10,1)), sg.InputText(key='cor', size=(15,1))],
                    [sg.Text("Tipo:", size=(10, 1)), sg.InputText(key='tipo', size=(15, 1))],
                    [sg.Text("Descrição:", size=(10, 1)), sg.InputText(key='descricao', size=(15, 2))],
                    [sg.Submit("Alterar", key='alterar', button_color='gray'), sg.Cancel("Cancelar", button_color='red', key='cancel')]
                ]

        super().__init__(sg.Window("Alteração de produto", layout=layout, resizable=False, finalize=True), (50,50))


    def open(self):
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
                        else:
                            try:
                                if valores['nome'].isascii() == False or valores['nome'].isnumeric() == True:
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
                                    super().close()
                                    break

                            except ValorInvalidoException as e:
                                super().show_message('Código inválido!', e)
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