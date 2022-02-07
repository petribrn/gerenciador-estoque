from limite.tela import Tela

class TelaEstoque(Tela):

  def trata_opcoes(self, msg: str = "", inteiros_validos: [] = None):
    valor = input(msg)
    try:
      inteiro = int(valor)
      if inteiros_validos and inteiro not in inteiros_validos:
        raise ValueError
      return inteiro
    except ValueError:
      print("\nValor invalido: digite novamente.")
      if inteiros_validos:
        print(f"Valores validos: {inteiros_validos}")

  def tela_opcoes(self):
    print("\n-------- ESTOQUE ----------")
    print("Escolha a opcao")
    print("1 - Fazer Movimentacao")
    print("2 - Listar Estoque")
    print("3 - Listar movimentações")
    print("4 - Listar movimentações de um usuário")
    print("0 - Retornar")

    opcao = self.trata_opcoes("Digite a opcao: ", [1,2,3,4,0])
    return opcao

  def pega_dados_movimentacao(self, lista_produtos: [], lista_usuarios: []):
    print("\n-------- TIPO MOVIMENTACAO ----------")
    print("1 - Adicionar")
    print("2 - Remover")

    tipo_input = self.trata_opcoes("\nDigite a opcao: ", [1,2])
    tipo = "adicionar" if tipo_input == 1 else "remover"

    codigos_produto = []
    codigos_usuario = []
    dados_movimentacao = {}

    dados_movimentacao["tipo"] = tipo

    for usuario in lista_usuarios:
      codigos_usuario.append(usuario.codigo)

    for produto in lista_produtos:
      codigos_produto.append(produto.codigo)

    print("\n-------- DADOS MOVIMENTACAO ----------")

    while True:
      codigo_produto = input("Codigo do produto: ")
      try:
        if codigo_produto.isnumeric() == False:
          raise ValueError
        if int(codigo_produto) not in codigos_produto:
          raise Exception
        dados_movimentacao["codigo_produto"] = int(codigo_produto)
        break
      except ValueError:
        print("\nDigite um valor valido!")
        print("O codigo nao deve conter letras e caracteres especiais.\n")
      except Exception:
        print("\nO codigo de produto nao esta cadastrado!")

    while True:
      codigo_usuario = input("Codigo do usuario: ")
      try:
        if codigo_usuario.isnumeric() == False:
          raise ValueError
        if int(codigo_usuario) not in codigos_usuario:
          raise Exception
        dados_movimentacao["codigo_usuario"] = int(codigo_usuario)
        break
      except ValueError:
        print("\nDigite um valor valido!")
        print("O codigo nao deve conter letras e caracteres especiais.\n")
      except Exception:
        print("\nO codigo de usuario nao esta cadastrado!")

    while True:
      quantidade = input("Quantidade: ")
      try:
        if quantidade.isnumeric() == False:
          raise ValueError
        dados_movimentacao["quantidade"] = int(quantidade)
        break
      except ValueError:
        print("\nDigite um valor valido!")
        print("O codigo nao deve conter letras e caracteres especiais.\n")

    return dados_movimentacao

  def mostra_produto(self, dados_produto):
    print("NOME DO PRODUTO: ", dados_produto['nome'])
    print("CODIGO DO PRODUTO: ", dados_produto['codigo'])
    print("QUANTIDADE EM ESTOQUE: ", dados_produto["quantidade"])
    print("\n")
  
  def mostra_movimentacao(self, dados_produto):
    print("CODIGO DA MOVIMENTACAO: ", dados_produto["codigo"])
    print("NOME DO PRODUTO: ", dados_produto["nome_produto"])
    print("CODIGO DO PRODUTO: ", dados_produto["codigo_produto"])
    print("NOME USUARIO: ", dados_produto["nome_usuario"])
    print("CODIGO USUARIO: ", dados_produto["codigo_usuario"])
    print("QUANTIDADE: ", dados_produto["quantidade"])
    print("\n")

  def seleciona_produto(self):
    codigo = int(input("Código do produto que deseja selecionar: "))
    return codigo

  def seleciona_usuario(self):
    codigo = int(input("Código do usuario que deseja selecionar: "))
    return codigo

  def seleciona_movimentacao(self):
    codigo = int(input("Código da movimentacao que deseja selecionar: "))
    return codigo

  def mostra_mensagem(self, msg):
    print(msg)