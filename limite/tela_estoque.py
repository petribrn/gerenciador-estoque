class TelaEstoque():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- ESTOQUE ----------")
    print("Escolha a opcao")
    print("1 - Incluir Produto")
    print("2 - Alterar Produto")
    print("3 - Listar Produtos")
    print("4 - Excluir Produto")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_produto(self):
    print("-------- DADOS PRODUTO ----------")
    titulo = input("Titulo: ")
    codigo = input("Codigo: ")

    return {"titulo": titulo, "codigo": codigo}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_produto(self, dados_produto):
    print("TITULO DO PRODUTO: ", dados_produto["titulo"])
    print("CODIGO DO PRODUTO: ", dados_produto["codigo"])
    print("\n")

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_produto(self):
    codigo = input("Código do produto que deseja selecionar: ")
    return codigo

  def mostra_mensagem(self, msg):
    print(msg)
