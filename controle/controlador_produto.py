from limite.tela_produto import TelaProduto
from entidade.produto import Produto

class ControladorProduto():
    def __init__(self, controlador_sistema):
        self.__produtos = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_produto = TelaProduto()

    def adiciona_produto(self):
        dados_produto = self.__tela_produto.pega_dados_produto(self.__produtos)
        produto = Produto(dados_produto["nome"], dados_produto["cor"], dados_produto["tipo"], dados_produto["descricao"], dados_produto["codigo"])
        self.__produtos.append(produto)

    def exclui_produto(self):
        self.__tela_produto.mostra_mensagem("\n-------- EXCLUIR PRODUTO --------")
        self.lista_produtos()

        if len(self.__produtos) < 1:
            pass
        else:
            codigo_produto = self.__tela_produto.seleciona_produto()
            produto = self.pega_produto_por_codigo(codigo_produto)

            if produto is not None:
                self.__produtos.remove(produto)
                self.__tela_produto.mostra_mensagem("\nProduto excluido.\n")
            else:
                self.__tela_produto.mostra_mensagem("\nProduto inexistente!\n")

    def altera_produto(self):
        self.__tela_produto.mostra_mensagem("\n-------- ALTERAR PRODUTO --------")
        self.lista_produtos()

        if len(self.__produtos) < 1:
            pass
        else:
            codigo_produto = self.__tela_produto.seleciona_produto()
            produto = self.pega_produto_por_codigo(codigo_produto)

            if produto is not None:
                novos_dados_produto = self.__tela_produto.pega_dados_produto(self.__produtos)
                produto.nome = novos_dados_produto["nome"]
                produto.cor = novos_dados_produto["cor"]
                produto.tipo = novos_dados_produto["tipo"]
                produto.descricao = novos_dados_produto["descricao"]
                produto.codigo = novos_dados_produto["codigo"]
                self.lista_produtos()
            else:
                self.__tela_produto.mostra_mensagem("\nProduto inexistente!\n")

    def lista_um_produto(self):
        if len(self.__produtos) < 1:
            self.__tela_produto.mostra_mensagem("\nNao existem produtos cadastrados.")
            self.__tela_produto.mostra_mensagem("Primeiro cadastre um produto!\n")
        else:
            codigo_produto = self.__tela_produto.seleciona_produto()
            produto = self.pega_produto_por_codigo(codigo_produto)

            if produto is not None:
                self.__tela_produto.mostra_mensagem("\nProduto encontrado:\n")
                self.__tela_produto.mostra_produto({"nome": produto.nome,"cor": produto.cor, "tipo": produto.tipo, "descricao": produto.descricao, "codigo": produto.codigo})
            else:
                self.__tela_produto.mostra_mensagem("Produto inexistente!\n")

    def lista_produtos(self):
        quantidade_produtos = len(self.__produtos)
        if quantidade_produtos < 1:
            self.__tela_produto.mostra_mensagem("\nNao existem produtos cadastrados.")
            self.__tela_produto.mostra_mensagem("Primeiro cadastre um produto!\n")
        else:
            self.__tela_produto.mostra_mensagem(f"\n{'Existe' if quantidade_produtos < 2 else 'Existem'} {quantidade_produtos} {'produtos cadastrados' if quantidade_produtos > 1 else 'produto cadastrado'}:\n")
            for produto in self.__produtos:
                self.__tela_produto.mostra_produto({"nome": produto.nome,"cor": produto.cor, "tipo": produto.tipo, "descricao": produto.descricao, "codigo": produto.codigo})

    def pega_produto_por_codigo(self, codigo):
        for produto in self.__produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adiciona_produto, 2: self.altera_produto, 3: self.lista_um_produto, 4: self.lista_produtos,5: self.exclui_produto, 0: self.retornar}

        continua = True
        while continua:
            try:
                lista_opcoes[self.__tela_produto.tela_opcoes()]()
            except Exception:
                pass