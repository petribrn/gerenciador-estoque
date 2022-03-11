import PySimpleGUI as sg
from entidade.usuario import Usuario
from persistencia.usuario_dao import UsuarioDAO
from limite.tela_usuario import TelaUsuario
from limite.tela_altera_usuario import TelaAlteraUsuario
from limite.tela_cadastro_usuario import TelaCadastroUsuario
from limite.tela_seleciona_codigo import TelaSelecionaCodigo
from limite.tela_remove_usuario import TelaRemoveUsuario
from limite.tela_lista_um_usuario import TelaListaUmUsuario
from limite.tela_lista_usuarios import TelaListaUsuarios

class ControladorUsuario:

    def __init__(self, controlador_sistema):
        self.__usuario_dao = UsuarioDAO()
        self.__tela_usuario = TelaUsuario()
        self.__tela_cadastro = TelaCadastroUsuario()
        self.__tela_seleciona_codigo = TelaSelecionaCodigo()
        self.__tela_altera_usuario = TelaAlteraUsuario()
        self.__tela_remove_usuario = TelaRemoveUsuario()
        self.__tela_lista_um_usuario = TelaListaUmUsuario()
        self.__tela_lista_usuarios = TelaListaUsuarios()
        self.__controlador_sistema = controlador_sistema

    @property
    def usuarios(self):
        return self.__usuario_dao.get_all()

    def inclui_usuario(self):
        self.__tela_cadastro.init_components()
        while True:
            botao, valores = self.__tela_cadastro.open(self.__usuario_dao.get_all_keys())

            if botao == 'incluir':
                if valores is not None:
                    usuario = Usuario(valores['nome'], valores['codigo'])
                    self.__usuario_dao.persist(usuario)
                    self.__tela_usuario.show_message('Usuário adicionado!', f'O usuário {usuario.codigo} - {usuario.nome} foi adicionado.')
                    break
            else:
                break

    def altera_usuario(self):
        if len(self.__usuario_dao.get_all()) < 1:
            self.__tela_usuario.show_message("Erro!", "Não existem usuários cadastrados!")
        else:
            self.__tela_seleciona_codigo.init_components()
            botao, codigo = self.__tela_seleciona_codigo.open()

            usuario_encontrado = None
            if botao == 'buscar':
                if codigo is not None and codigo in self.__usuario_dao.get_all_keys():
                    for usuario in self.__usuario_dao.get_all():
                        if usuario.codigo == codigo:
                            usuario_encontrado = usuario
                            self.__tela_usuario.show_message("Usuario encontrado!",
                                                             f"O usuário de código {codigo} foi encontrado.")
                            break
                    self.__tela_altera_usuario.init_components(usuario_encontrado)
                    while True:
                        botao, novo_nome = self.__tela_altera_usuario.open()
                        if botao == 'alterar':
                            if novo_nome is not None:
                                usuario_encontrado.nome = novo_nome
                                self.__usuario_dao.persist(usuario_encontrado)
                                self.__tela_altera_usuario.show_message("Alteração de usuário",
                                                                        'Usuário alterado com sucesso!')
                                break
                        else:
                            self.__tela_altera_usuario.show_message("Alteração de usuário", 'Operação cancelada!')
                            break
                else:
                    if botao != 'cancelar':
                        self.__tela_usuario.show_message("Erro!", "Codigo Inexistente!")


    def exclui_usuario(self):
        if len(self.__usuario_dao.get_all()) < 1:
            self.__tela_usuario.show_message('Erro!', 'Não existem usuários cadastrados!')
        else:
            self.__tela_seleciona_codigo.init_components()
            botao, codigo = self.__tela_seleciona_codigo.open()

            usuario_encontrado = None

            if botao == 'buscar':
                if codigo is not None and codigo in self.__usuario_dao.get_all_keys():
                    for usuario in self.__usuario_dao.get_all():
                        if usuario.codigo == codigo:
                            usuario_encontrado = usuario
                            self.__tela_usuario.show_message("Usuario encontrado!",
                                                             f"O usuário de código {codigo} foi encontrado.")
                            break
                    self.__tela_remove_usuario.init_components(usuario_encontrado)
                    while True:
                        botao = self.__tela_remove_usuario.open()

                        if botao == 'remover':
                            self.__usuario_dao.remove(usuario_encontrado)
                            self.__tela_remove_usuario.show_message('Remover usuário', 'Usuário removido com sucesso!')
                            self.__tela_remove_usuario.close()
                            break

                        elif botao == 'cancelar':
                            self.__tela_remove_usuario.show_message('Remover usuário', 'Operação cancelada!')
                            self.__tela_remove_usuario.close()
                            break

                        elif botao in ('cancelar', sg.WIN_CLOSED):
                            self.__tela_remove_usuario.show_message('Remover usuário', 'Operação cancelada!')
                            self.__tela_remove_usuario.close()
                            break

                else:
                    if botao != 'cancelar':
                        self.__tela_usuario.show_message("Erro!", "Codigo Inexistente!")

    def lista_um_usuario(self):
        if len(self.__usuario_dao.get_all()) < 1:
            self.__tela_usuario.show_message('Erro!', 'Não existem usuários cadastrados!')
        else:
            self.__tela_seleciona_codigo.init_components()
            botao, codigo = self.__tela_seleciona_codigo.open()

            usuario_encontrado = None

            if botao == 'buscar':
                if codigo is not None and codigo in self.__usuario_dao.get_all_keys():
                    for usuario in self.__usuario_dao.get_all():
                        if usuario.codigo == codigo:
                            usuario_encontrado = usuario
                            self.__tela_usuario.show_message("Usuario encontrado!",
                                                             f"O usuário de código {codigo} foi encontrado.")
                            break
                    self.__tela_lista_um_usuario.init_components(usuario_encontrado)
                    while True:
                        botao = self.__tela_lista_um_usuario.open()
                        if botao == 'ok' or botao == None:
                            self.__tela_lista_um_usuario.close()
                            break
                else:
                    if botao != 'cancelar':
                        self.__tela_usuario.show_message("Erro!", "Codigo Inexistente!")


    def lista_usuarios(self):
        if len(self.__usuario_dao.get_all()) < 1:
            self.__tela_usuario.show_message('Erro!', 'Não existem usuários cadastrados!')
        else:
            informacoes_tabela = []
            colunas = ['Código', 'Usuário']

            for usuario in self.__usuario_dao.get_all():
                informacoes_tabela.append([usuario.codigo, usuario.nome])
            self.__tela_lista_usuarios.init_components(informacoes_tabela, colunas)
            while True:
                botao = self.__tela_lista_usuarios.open()

                if botao == 'ok':
                    self.__tela_lista_usuarios.close()
                    break
                else:
                    self.__tela_lista_usuarios.close()
                    break


    def retornar(self):
        self.__tela_usuario.close()

    def sair(self):
        exit(0)

    def abre_tela(self):
        opcoes = {1: self.inclui_usuario, 2: self.altera_usuario,
                  3: self.exclui_usuario, 4: self.lista_um_usuario,
                  5: self.lista_usuarios, 6: self.retornar, 0: self.sair}

        while True:
            self.__tela_usuario.init_components()
            opcao_escolhida = self.__tela_usuario.tela_opcoes()
            self.__tela_usuario.close()

            if opcao_escolhida == 6 or opcao_escolhida == None or sg.WIN_CLOSED:
                self.__tela_usuario.close()
                break
            else:
                opcoes[opcao_escolhida]()