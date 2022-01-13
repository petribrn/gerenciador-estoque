from abc import ABC, abstractmethod

class Tela(ABC):

    @abstractmethod
    def __init__(self, controlador):
        self.__controlador = controlador
        pass

    #removido a funcao trata_opcoes

    @abstractmethod
    def tela_opcoes(self):
        pass