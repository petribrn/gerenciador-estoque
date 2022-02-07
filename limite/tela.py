from abc import ABC, abstractmethod

class Tela(ABC):

    @abstractmethod
    def trata_opcoes(self):
        pass

    @abstractmethod
    def tela_opcoes(self):
        pass