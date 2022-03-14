from abc import ABC, abstractmethod
import PySimpleGUI as sg

class Tela(ABC):

    @abstractmethod
    def __init__(self, window, tamanho):
        self.__window = window
        self.__window.set_min_size(tamanho)

    @abstractmethod
    def init_components(self):
        pass

    @abstractmethod
    def open(self):
        pass

    def close(self):
        self.__window.Close()

    def show_message(self, titulo: str, msg):
        sg.Popup(titulo, msg)

    def read(self):
        botao, valores = self.__window.Read()
        return botao, valores

    def tela_opcoes(self):
        return self.open()