from limite.tela import Tela

class TelaEstoque(Tela):
   
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
    print("-------- ESTOQUE ----------")
    print("Escolha a opcao")
    print("1 - Fazer Movimentacao")
    print("2 - Listar Estoque")
    print("3 - Listar movimentações")
    print("4 - Listar movimentações de um usuário")
    print("0 - Retornar")

    opcao = self.trata_opcoes("Digite a opcao: ", [1,2,3,4, 5,0])
    return opcao

  def pega_dados_movimentacao(self):
    print("Escolha a opcao")
    print("1 - Adicionar")
    print("2 - Remover")

    tipo_input = input()

    tipo = "adicionar" if tipo_input == "1" else "remover"

    print("-------- DADOS MOVIMENTACAO ----------")
    codigo_produto = input("Codigo do produto: ")
    codigo_usuario = input("Codigo do usuario: ")
    quantidade = int(input("Codigo do usuario: "))

    return {codigo_produto: codigo_produto, codigo_usuario: codigo_usuario, quantidade: quantidade, tipo: tipo}

  def mostra_produto(self, dados_produto):
    print("TITULO DO PRODUTO: ", dados_produto["titulo"])
    print("CODIGO DO PRODUTO: ", dados_produto["codigo"])
    print("QUANTIDADE EM ESTOQUE: ", dados_produto["quantidade"])
    print("\n")
  
  def mostra_movimentacao(self, dados_produto):
    print("CODIGO DA MOVIMENTACAO: ", dados_produto["codigo"])
    print("TITULO DO PRODUTO: ", dados_produto["titulo_produto"])
    print("CODIGO DO PRODUTO: ", dados_produto["codigo_produto"])
    print("NOME USUARIO: ", dados_produto["nome_usuario"])
    print("CODIGO USUARIO: ", dados_produto["codigo_usuario"])
    print("\n")

  def seleciona_produto(self):
    codigo = input("Código do produto que deseja selecionar: ")
    return codigo

  def seleciona_usuario(self):
    codigo = input("Código do usuario que deseja selecionar: ")
    return codigo

  def seleciona_movimentacao(self):
    codigo = input("Código da movimentacao que deseja selecionar: ")
    return codigo

  def mostra_mensagem(self, msg):
    print(msg)
