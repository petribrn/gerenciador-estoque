class TipoInvalidoException(Exception):
    def __init__(self):
        super().__init__("\nDigite um tipo válido:\nO tipo deve ter no mínimo 2 caracteres..\nO tipo não deve conter números e caracteres especiais.\n")