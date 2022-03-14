class CodigoInexistenteException(Exception):
    def __init__(self, codigo: str):
        super().__init__(f"\nO codigo {codigo} é inexistente!")