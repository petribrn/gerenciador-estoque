from limite.tela_produto import TelaProduto
from entidade.produto import Produto

class ControladorProduto():
    def __init__(self, controlador_sistema):
        self.__produtos = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_produto = TelaProduto

    def adiciona_produto(self):
        dados_produto = self.__tela_produto.pega_dados_produto()
        produto = Produto(dados_produto["nome"], dados_produto["cor"], dados_produto["tipo"], dados_produto["descricao"], dados_produto["codigo"])
        self.__produtos.append(produto)

    def exclui_produto(self):
        self.lista_produto()
        codigo_produto = self.__tela_produto.seleciona_produto()
        produto = self.pega_produto_por_codigo(codigo_produto)

        if produto is not None:
            self.__produtos.remove(produto)
            self.lista_produto()
        else:
            self.__tela_produto.mostra_mensagem(msg="Produto inexistente!")

    def altera_produto(self):
        self.lista_produto()
        codigo_produto = self.__tela_produto.seleciona_produto()
        produto = self.pega_produto_por_codigo(codigo_produto)

        if produto is not None:
            novos_dados_produto = self.__tela_produto.pega_dados_produto()
            produto.nome = novos_dados_produto["nome"]
            produto.cor = novos_dados_produto["cor"]
            produto.tipo = novos_dados_produto["tipo"]
            produto.descricao = novos_dados_produto["descricao"]
            produto.codigo = novos_dados_produto["codigo"]
            self.lista_produto()
        else:
            self.__tela_produto.mostra_mensagem(msg="Produto inexistente!")

    def lista_produto(self):
        if len(self.__produtos) > 0:
            for produto in self.__produtos:
                self.__tela_produto.mostra_produto({"nome": produto.nome, "cor": produto.tipo, "tipo": produto.descricao, "descricao": produto.descricao, "codigo": produto.codigo})
        else:
            print("A lista de produtos está vazia.")

    def pega_produto_por_codigo(self, codigo):
        for produto in self.__produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def retornar(self):
        self.__controlador_sistema.abre_tela() #Necessário implementação Victor Hugo

    def abre_tela(self):
        lista_opcoes = {1: self.adiciona_produto, 2: self.exclui_produto, 3: self.lista_produto, 4: self.altera_produto, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_produto.tela_opcoes()]()