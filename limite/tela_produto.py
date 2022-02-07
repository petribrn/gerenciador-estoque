from limite.tela import Tela

class TelaProduto(Tela):

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
        print("1 - Adicionar produto")
        print("2 - Excluir produto")
        print("3 - Listar produtos")
        print("4 - Alterar produto")
        print("0 - Retornar")

        opcao = self.trata_opcoes("Digite a opcao: ", [1,2,3,4,0])
        return opcao

    def pega_dados_produto(self):
        print("-----DADOS DO PRODUTO-----")

        while True:
            produto = {}
            try:
                nome = input("Nome: ")
                if not isinstance(nome, str):
                    raise ValueError
                else:
                    produto["nome"] = nome
            except ValueError:
                print("Digite um nome válido!")

            try:
                cor = input("Cor: ")
                if not isinstance(cor, str):
                    raise ValueError
                else:
                    produto["cor"] = cor
            except ValueError:
                print("Digite uma cor válida!")

            try:
                tipo = input("Tipo: ")
                if not isinstance(tipo, str):
                    raise ValueError
                else:
                    produto["tipo"] = tipo
            except ValueError:
                print("Digite um tipo válido!")

            try:
                descricao = input("Descrição: ")
                if not isinstance(descricao, str):
                    raise ValueError
                else:
                    produto["descricao"] = descricao
            except ValueError:
                print("Digite uma descrição válida!")

            try:
                codigo = input("Código: ")
                if not isinstance(codigo, str):
                    raise ValueError
                else:
                    produto["codigo"] = codigo
            except ValueError:
                print("Digite um código válido!")

            return produto

    def mostra_produto(self, dados_produto):
        print(f"NOME DO PRODUTO: {dados_produto['nome']}")
        print(f"COR: {dados_produto['cor']}")
        print(f"TIPO: {dados_produto['tipo']}")
        print(f"DESCRIÇÃO: {dados_produto['descricao']}")
        print(f"CÓDIGO: {dados_produto['codigo']}")
        print('\n')

    def seleciona_produto(self):
        codigo = input("Digite o código do produto: ")
        return codigo

    def mostra_mensagem(self, msg: str):
        print(msg)





