from limite.tela import Tela

class TelaSistema(Tela):
    def trata_opcoes(self, msg: str = "", inteiros_validos = None):
        valor = input(msg)
        try:
            inteiro = int(valor)
            if inteiros_validos and inteiro not in inteiros_validos:
                raise ValueError
        except ValueError:
            print("Valor inválido: digite novamente.")
            if inteiros_validos:
                print(f"Valores válidos: {inteiros_validos}")

    def tela_opcoes(self):
        print("-------- GERENCIADOR ---------")
        print("Escolha sua opcao")
        print("1 - Usuários")
        print("2 - Produtos")
        print("3 - Movimentações")
        print("0 - Finalizar sistema")
        opcao = self.trata_opcoes("Digite a opcao: ", [1,2,3,0])
        return opcao
