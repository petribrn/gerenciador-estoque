class CorInvalidaException(Exception):
    def __init__(self):
        super().__init__("\nDigite uma cor válida:\nA cor deve ter no mínimo 2 caracteres..\nA cor não deve conter números e caracteres especiais.\n")