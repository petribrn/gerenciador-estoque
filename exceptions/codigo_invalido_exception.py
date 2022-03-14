class CodigoInvalidoException(Exception):
    def __init__(self):
        super().__init__("\nDigite um código valido:\nO código não deve conter letras e caracteres especiais.\n")