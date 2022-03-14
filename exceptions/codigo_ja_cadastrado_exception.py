class CodigoJaCadastradoException(Exception):
    def __init__(self, codigo: str):
        super().__init__(f"\nO codigo {codigo} ja esta cadastrado!")