class TelaSistema:
    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("-------- GERENCIADOR ---------")
        print("Escolha sua opcao")
        print("1 - Usuários")
        print("2 - Produtos")
        print("3 - Movimentações")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao:"))
        return opcao
