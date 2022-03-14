import PySimpleGUI as sg
from limite.abstract_tela import Tela
from exceptions.entrada_vazia_exception import EntradaVaziaException
from exceptions.nome_invalido_exception import NomeInvalidoException


class TelaAlteraUsuario(Tela):

    def __init__(self):
        pass

    def init_components(self, usuario):

        sg.theme("Reddit")
        layout = [
                    [sg.Text(f"Alterar usuário de código {usuario.codigo}:")],
                    [sg.Text(f"Nome: {usuario.nome}")],
                    [sg.Text('Novos dados do usuário:')],
                    [sg.Text("Nome:", size=(10,1)), sg.InputText(key='novo_nome', size=(18,1))],
                    [sg.Submit("Alterar", key='alterar', button_color='gray'), sg.Cancel("Cancelar", button_color='red', key='cancel')]
                ]

        super().__init__(sg.Window("Alteração de Usuário", layout=layout, resizable=False, finalize=True), (50,80))

    def open(self):
        while True:
            botao, valores = super().read()
            if botao == 'alterar':
                try:
                    if valores is not None and valores['novo_nome'] != '' and valores['novo_nome'] is not None:
                        try:
                            if valores['novo_nome'].isascii() == False or valores['novo_nome'].isnumeric() == True:
                                raise NomeInvalidoException

                            elif len(valores['novo_nome']) < 2 or len(valores['novo_nome']) > 15:
                                raise NomeInvalidoException # criar exception para strings invalidas

                            else:
                                valores['novo_nome'] = valores['novo_nome']
                                super().close()
                                break

                        except NomeInvalidoException as e:
                            super().show_message('Nome inválido!', e)
                    else:
                        raise EntradaVaziaException

                except EntradaVaziaException as f:
                    super().show_message('Campos incompletos!', f)

            elif botao == 'cancel':
                super().close()
                break

            elif botao in ('cancel', sg.WIN_CLOSED):
                super().close()
                break

        return botao, valores['novo_nome']