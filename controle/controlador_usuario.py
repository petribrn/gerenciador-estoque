from limite.tela_usuario import TelaUsuario
from entidade.usuario import Usuario


class ControladorUsuario:
    def __init__(self, controlador_sistema):
        self.__usuarios = []
        self.__tela_usuario = TelaUsuario()
        self.__controlador_sistema = controlador_sistema

    @property
    def usuarios(self):
        return self.__usuarios

    def inclui_usuario(self):
        dados_usuario = self.__tela_usuario.pega_dados_usuario(self.__usuarios)
        usuario = Usuario(dados_usuario["nome"], dados_usuario["codigo"])
        self.__usuarios.append(usuario)

    def exclui_usuario(self):
        self.__tela_usuario.mostra_mensagem("\n-------- EXCLUIR USUARIO --------")
        self.lista_usuarios()
        if len(self.__usuarios) < 1:
            pass
        else:
            codigo_usuario = self.__tela_usuario.seleciona_usuario()
            usuario = self.pega_usuario_por_codigo(codigo_usuario)

            if usuario is not None:
                self.__usuarios.remove(usuario)
                self.__tela_usuario.mostra_mensagem("\nUsuario excluido.\n")
            else:
                self.__tela_usuario.mostra_mensagem("\nUsuario inexistente!\n")

    def altera_usuario(self):
        self.__tela_usuario.mostra_mensagem("\n-------- ALTERAR USUARIO --------")
        self.lista_usuarios()
        if len(self.__usuarios) < 1:
            pass
        else:
            codigo_usuario = self.__tela_usuario.seleciona_usuario()
            usuario = self.pega_usuario_por_codigo(codigo_usuario)

            if usuario is not None:
                novos_dados_usr = self.__tela_usuario.pega_dados_usuario(self.__usuarios)
                usuario.nome = novos_dados_usr["nome"]
                usuario.codigo = novos_dados_usr["codigo"]
                self.lista_usuarios()
            else:
                self.__tela_usuario.mostra_mensagem("\nUsuario inexistente!\n")

    def lista_um_usuario(self):

        if len(self.__usuarios) < 1:
            self.__tela_usuario.mostra_mensagem("\nNao existem usuarios cadastrados.")
            self.__tela_usuario.mostra_mensagem("Primeiro cadastre um usuario!\n")
        else:
            codigo_usuario = self.__tela_usuario.seleciona_usuario()
            usuario = self.pega_usuario_por_codigo(codigo_usuario)

            if usuario is not None:
                self.__tela_usuario.mostra_mensagem("\nUsuario encontrado:\n")
                self.__tela_usuario.mostra_usuario({"nome": usuario.nome, "codigo": usuario.codigo})
            else:
                self.__tela_usuario.mostra_mensagem("Usuario inexistente!\n")

    def lista_usuarios(self):
        quantidade_usuarios = len(self.__usuarios)
        if quantidade_usuarios < 1:
            self.__tela_usuario.mostra_mensagem("\nNao existem usuarios cadastrados.")
            self.__tela_usuario.mostra_mensagem("Primeiro cadastre um usuario!\n")
        else:
            self.__tela_usuario.mostra_mensagem(f"\n{'Existe' if quantidade_usuarios < 2 else 'Existem'} {quantidade_usuarios} {'usuarios cadastrados' if quantidade_usuarios > 1 else 'usuario cadastrado'}:\n")
            for usuario in self.__usuarios:
                self.__tela_usuario.mostra_usuario({"nome": usuario.nome, "codigo": usuario.codigo})

    def pega_usuario_por_codigo(self, codigo_usuario):
        for usuario in self.__usuarios:
            if usuario.codigo == codigo_usuario:
                return usuario
        return None

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_usuario, 2: self.altera_usuario, 3: self.lista_um_usuario,
                        4: self.lista_usuarios,
                        5: self.exclui_usuario, 0: self.retornar}

        continua = True
        while continua:
            try:
                lista_opcoes[self.__tela_usuario.tela_opcoes()]()
            except Exception:
                 pass
