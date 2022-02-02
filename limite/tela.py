from abc import ABC, abstractmethod

class Tela(ABC):

    @abstractmethod
    def __init__(self, controlador):
        self.__controlador = controlador
        pass

    @abstractmethod
    def trata_opcoes(self):
        pass

    @abstractmethod
    def tela_opcoes(self):
        pass