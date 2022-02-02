from limite.tela import Tela
from controle.controlador_usuario import ControladorUsuario

class TelaUsuario(Tela):
    def __init__(self):
        self.__controlador = ControladorUsuario

    def trata_opcoes(self, msg: str = "", inteiros_validos: [] = None):
        valor = input(msg)
        try:
            inteiro = int(valor)
            if inteiros_validos and inteiro not in inteiros_validos:
                raise ValueError
        except ValueError:
            print("Valor inválido: digite novamente.")
            if inteiros_validos:
                print(f"Valores válidos: {inteiros_validos}")

    def tela_opcoes(self):
        print("-------- PRODUTOS ----------")
        print("1 - Incluir usuario")
        print("2 - Alterar usuario")
        print("3 - Listar um usuario")
        print("4 - Listar todos os usuarios")
        print("5 - Excluir usuario")
        print("0 - Retornar")

        opcao = self.trata_opcoes("Digite a opcao: ", [1,2,3,4,0])
        return opcao

    def pega_dados_usuario(self):
        print("-----DADOS DO USUARIO-----")

        while True:
            usuario = {}
            try:
                nome = input("Nome: ")
                if not isinstance(nome, str):
                    raise ValueError
                else:
                    usuario["nome"] = nome
            except ValueError:
                print("Digite um nome válido!")

            try:
                codigo = input("Código: ")
                if not isinstance(codigo, str):
                    raise ValueError
                else:
                    usuario["codigo"] = codigo
            except ValueError:
                print("Digite um código válido!")

            return usuario

    def mostra_usuario(self, dados_usuario):
        print(f"NOME DO USUARIO: {dados_usuario['nome']}")
        print(f"CÓDIGO: {dados_usuario['codigo']}")
        print('\n')

    def seleciona_usuario(self):
        codigo = input("Digite o código do usuario: ")
        return codigo

    def mostra_mensagem(self, msg: str):
        print(msg)





