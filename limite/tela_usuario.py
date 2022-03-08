from limite.tela import Tela

class TelaUsuario(Tela):

    def __init__(self):
        super().__init__()

    def tela_opcoes(self):
        print("\n-------- USUARIOS --------")
        print("1 - Incluir usuario")
        print("2 - Alterar usuario")
        print("3 - Listar um usuario")
        print("4 - Listar todos os usuarios")
        print("5 - Excluir usuario")
        print("0 - Retornar")

        opcao = super().trata_opcoes("\nDigite a opcao: ", [1,2,3,4,5,0])
        return opcao

    def pega_dados_usuario(self, lista_de_usuarios: []):
        print("\n-----DADOS DO USUARIO-----")
        usuario = {}
        codigos = []

        for user in lista_de_usuarios:
            codigos.append(user.codigo)

        while True:
            nome = input("Nome: ")
            try:
                if nome.isascii() == False or nome.isnumeric() == True:
                    raise ValueError
                if len(nome) < 2 or len(nome) > 15:
                    raise ValueError
                usuario["nome"] = nome
                break
            except ValueError:
                print("\nDigite um nome valido!")
                print("O nome deve ter de 2 a 15 caracteres.")
                print("O nome nao deve conter apenas numeros.\n")

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
                print("O codigo nao deve conter letras e caracteres especiais.\n")
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
                print("\nDigite um valor valido!")

    def mostra_mensagem(self, msg: str):
        print(msg)





