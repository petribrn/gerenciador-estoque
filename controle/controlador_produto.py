from limite.tela_produto import TelaProduto
from entidade.produto import Produto
from persistencia.produto_dao import ProdutoDAO

class ControladorProduto():
    def __init__(self, controlador_sistema):
        self.__produto_dao = ProdutoDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_produto = TelaProduto()

    @property
    def produtos(self):
        return self.__produto_dao.get_all()

    def adiciona_produto(self):
        dados_produto = self.__tela_produto.pega_dados_produto(self.__produto_dao.get_all())
        produto = Produto(dados_produto["nome"], dados_produto["cor"], dados_produto["tipo"], dados_produto["descricao"], dados_produto["codigo"])
        self.__produto_dao.persist(produto)

    def exclui_produto(self):
        self.__tela_produto.mostra_mensagem("\n-------- EXCLUIR PRODUTO --------")
        self.lista_produtos()

        if len(self.__produto_dao.get_all()) < 1:
            pass
        else:
            codigo_produto = self.__tela_produto.seleciona_produto()
            produto = self.pega_produto_por_codigo(codigo_produto)

            if produto is not None:
                self.__produto_dao.remove(produto)
                self.__tela_produto.mostra_mensagem("\nProduto excluido.\n")
            else:
                self.__tela_produto.mostra_mensagem("\nProduto inexistente!\n")

    def altera_produto(self):
        self.__tela_produto.mostra_mensagem("\n-------- ALTERAR PRODUTO --------")
        self.lista_produtos()

        if len(self.__produto_dao.get_all()) < 1:
            pass
        else:
            codigo_produto = self.__tela_produto.seleciona_produto()
            produto = self.pega_produto_por_codigo(codigo_produto)

            if produto is not None:
                novos_dados_produto = self.__tela_produto.pega_dados_produto(self.__produto_dao.get_all())
                produto.nome = novos_dados_produto["nome"]
                produto.cor = novos_dados_produto["cor"]
                produto.tipo = novos_dados_produto["tipo"]
                produto.descricao = novos_dados_produto["descricao"]
                produto.codigo = novos_dados_produto["codigo"]
                self.__produto_dao.persist(produto)
                self.lista_produtos()
            else:
                self.__tela_produto.mostra_mensagem("\nProduto inexistente!\n")

    def lista_um_produto(self):
        if len(self.__produto_dao.get_all()) < 1:
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
        quantidade_produtos = len(self.__produto_dao.get_all())
        if quantidade_produtos < 1:
            self.__tela_produto.mostra_mensagem("\nNao existem produtos cadastrados.")
            self.__tela_produto.mostra_mensagem("Primeiro cadastre um produto!\n")
        else:
            self.__tela_produto.mostra_mensagem(f"\n{'Existe' if quantidade_produtos < 2 else 'Existem'} {quantidade_produtos} {'produtos cadastrados' if quantidade_produtos > 1 else 'produto cadastrado'}:\n")
            for produto in self.__produto_dao.get_all():
                self.__tela_produto.mostra_produto({"nome": produto.nome,"cor": produto.cor, "tipo": produto.tipo, "descricao": produto.descricao, "codigo": produto.codigo})

    def pega_produto_por_codigo(self, codigo):
        for produto in self.__produto_dao.get_all():
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