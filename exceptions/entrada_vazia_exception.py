class EntradaVaziaException(Exception):
    def __init__(self,):
        super().__init__(f"\nUm ou mais campos estão vazios!\nPreencha todos os campos antes de prosseguir...")