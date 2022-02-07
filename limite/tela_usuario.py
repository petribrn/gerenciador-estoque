from limite.tela import Tela

class TelaUsuario(Tela):

    def trata_opcoes(self, msg: str = "", inteiros_validos: [] = None):
        valor = input(msg)
        try:
            inteiro = int(valor)
            if inteiros_validos and inteiro not in inteiros_validos:
                raise ValueError
            return inteiro
        except ValueError:
            print("\nValor inválido: digite novamente.")
            if inteiros_validos:
                print(f"Valores válidos: {inteiros_validos}")

    def tela_opcoes(self):
        print("\n-------- USUARIOS --------")
        print("1 - Incluir usuario")
        print("2 - Alterar usuario")
        print("3 - Listar um usuario")
        print("4 - Listar todos os usuarios")
        print("5 - Excluir usuario")
        print("0 - Retornar")

        opcao = self.trata_opcoes("\nDigite a opcao: ", [1,2,3,4,5,0])
        return opcao

    def pega_dados_usuario(self, lista_de_usuarios):
        print("\n-----DADOS DO USUARIO-----")
        usuario = {}
        codigos = []

        for user in lista_de_usuarios:
            codigos.append(user.codigo)

        while True:
            nome = input("Nome: ")
            try:
                int(nome)
                print("\nDigite um nome valido!")
            except ValueError:
                usuario["nome"] = nome
                break
        while True:
            codigo = input("Codigo: ")
            try:
                if codigo.isnumeric() == False:
                    raise ValueError
                if int(codigo) in codigos:
                    raise Exception
                usuario["codigo"] = int(codigo)
                break
            except ValueError:
                print("\nDigite um valor valido!")
            except Exception:
                print("\nO codigo ja esta cadastrado!")

        return usuario

    def mostra_usuario(self, dados_usuario):
        print("-"*18 + ("-"*len(dados_usuario["nome"])))
        print(f"NOME DO USUARIO: {dados_usuario['nome']}")
        print(f"CODIGO: {dados_usuario['codigo']}")
        print("-" * 18 + ("-" * len(dados_usuario["nome"]))+"\n")


    def seleciona_usuario(self):
        while True:
            codigo = input("\nDigite o codigo do usuario: ")
            try:
                if codigo.isnumeric() == False:
                    raise ValueError
                return int(codigo)
            except ValueError:
                print("Digite um valor valido!")

    def mostra_mensagem(self, msg: str):
        print(msg)





