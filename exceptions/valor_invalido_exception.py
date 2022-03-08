class ValorInvalidoException(Exception):
    def __init__(self):
        super().__init__("\nDigite um valor valido!\nO codigo nao deve conter letras e caracteres especiais.\n")