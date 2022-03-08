from limite.tela import Tela

class TelaSistema(Tela):

    def __init__(self):
        super().__init__()

    def tela_opcoes(self):
        print("-------- GERENCIADOR ---------")
        print("Escolha sua opcao")
        print("1 - Usuários")
        print("2 - Produtos")
        print("3 - Movimentações")
        print("0 - Finalizar sistema")
        opcao = super().trata_opcoes("Digite a opcao: ", [1,2,3,0])
        return opcao