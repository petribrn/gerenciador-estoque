class DescricaoInvalidaException(Exception):
    def __init__(self):
        super().__init__("\nDigite uma descrição válida:\nA descrição deve ter de 2 a 30 caracteres.\nA descricao não deve conter apenas números.\n")