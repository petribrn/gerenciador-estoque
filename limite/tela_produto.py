from limite.tela import Tela

class TelaProduto(Tela):

    def __init__(self):
        super().__init__()

    def tela_opcoes(self):
        print("\n-------- PRODUTOS --------")
        print("1 - Adicionar produto")
        print("2 - Alterar produto")
        print("3 - Listar um produto")
        print("4 - Listar todos os produtos")
        print("5 - Excluir produto")
        print("0 - Retornar")

        opcao = super().trata_opcoes("\nDigite a opcao: ", [1,2,3,4,5,0])
        return opcao

    def pega_dados_produto(self, lista_de_produtos: []):
        print("\n-----DADOS DO PRODUTO-----")
        produto = {}
        codigos = []

        for product in lista_de_produtos:
            codigos.append(product.codigo)

        while True:
            nome = input("Nome: ")
            try:
                if nome.isascii() == False or nome.isnumeric() == True:
                    raise ValueError
                if len(nome) < 2 or len(nome) > 15:
                    raise ValueError
                produto["nome"] = nome
                break
            except ValueError:
                print("\nDigite um nome valido!")
                print("O nome deve ter de 2 a 15 caracteres.")
                print("O nome nao deve conter apenas numeros.\n")
        while True:
            cor = input("Cor: ")
            try:
                if cor.isalpha() == False:
                    raise ValueError
                if len(cor) < 2:
                    raise ValueError
                produto["cor"] = cor
                break
            except ValueError:
                print("\nDigite uma cor valida!")
                print("A cor deve ter no minimo 2 caracteres.")
                print("A cor nao deve conter numeros e caracteres especiais.\n")

        while True:
            tipo = input("Tipo: ")
            try:
                if tipo.isalpha() == False:
                    raise ValueError
                if len(tipo) < 2:
                    raise ValueError
                produto["tipo"] = tipo
                break
            except ValueError:
                print("\nDigite um tipo valido!")
                print("O tipo deve ter no minimo 2 caracteres")
                print("O tipo nao deve conter numeros e caracteres especiais.\n")

        while True:
            descricao = input("Descricao: ")
            try:
                if descricao.isascii() == False and descricao.isnumeric() == True:
                    raise ValueError
                if len(descricao) < 2 or len(descricao) > 30:
                    raise ValueError
                produto["descricao"] = descricao
                break
            except ValueError:
                print("\nDigite uma descricao valida!")
                print("A descricao deve ter de 2 a 30 caracteres.")
                print("A descricao nao deve conter apenas numeros.\n")

        while True:
            codigo = input("Codigo: ")
            try:
                if codigo.isnumeric() == False:
                    raise ValueError
                if int(codigo) in codigos:
                    raise Exception
                produto["codigo"] = int(codigo)
                break
            except ValueError:
                print("\nDigite um valor valido!")
                print("O codigo nao deve conter letras e caracteres especiais.\n")
            except Exception:
                print("\nO codigo ja esta cadastrado!")

        return produto

    def mostra_produto(self, dados_produto):
        print("-" * 12 + ("-" * len(dados_produto["descricao"])))
        print(f"NOME DO PRODUTO: {dados_produto['nome']}")
        print(f"COR: {dados_produto['cor']}")
        print(f"TIPO: {dados_produto['tipo']}")
        print(f"DESCRICAO: {dados_produto['descricao']}")
        print(f"CODIGO: {dados_produto['codigo']}")
        print("-" * 12 + ("-" * len(dados_produto["descricao"]))+"\n")


    def seleciona_produto(self):
        while True:
            codigo = input("\nDigite o codigo do produto: ")
            try:
                if codigo.isnumeric() == False:
                    raise ValueError
                return int(codigo)
            except ValueError:
                print("\nDigite um valor valido!")
                print("O codigo nao deve conter letras e caracteres especiais.\n")


    def mostra_mensagem(self, msg: str):
        print(msg)





