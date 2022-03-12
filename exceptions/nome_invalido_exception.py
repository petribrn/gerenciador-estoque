class NomeInvalidoException(Exception):
    def __init__(self):
        super().__init__("\nDigite um nome válido:\nO nome deve ter de 2 a 15 caracteres.\nO nome não deve conter apenas numeros.\n")