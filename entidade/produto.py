class Produto:
    def __init__(self,nome: str, cor: str, tipo: str, descricao: str, codigo: int):
        self.__nome = None
        self.__cor = None
        self.__tipo = None
        self.descricao = None
        self.__codigo = None
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(cor, str):
            self.__cor = cor
        if isinstance(tipo, str):
            self.__tipo = tipo
        if isinstance(descricao, str):
            self.__descricao = descricao
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def nome(self):
        return  self.__nome
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def cor(self):
        return self.__cor
    @cor.setter
    def cor(self, cor: str):
        if isinstance(cor, str):
            self.__cor = cor

    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, tipo: str):
        if isinstance(tipo, str):
            self.__tipo = tipo

    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self, descricao: str):
        if isinstance(descricao, str):
            self.__descricao = descricao

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo