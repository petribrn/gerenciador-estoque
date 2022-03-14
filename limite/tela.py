from abc import ABC, abstractmethod

class Tela(ABC):

    @abstractmethod
    def __init__(self):
        pass

    def trata_opcoes(self, msg, inteiros_validos):
        valor = input(msg)
        try:
            inteiro = int(valor)
            if inteiros_validos and inteiro not in inteiros_validos or inteiro == None or inteiro == '':
                raise ValueError
            return inteiro
        except ValueError:
            print("\nValor invalido: digite novamente.")
            if inteiros_validos:
                print(f"Valores validos: {inteiros_validos}")

    @abstractmethod
    def tela_opcoes(self):
        pass