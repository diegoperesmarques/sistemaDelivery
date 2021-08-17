def ultimoCodigoProdutoCadastrado():
    with open('cadastroProduto.txt', 'r', encoding='utf-8') as listaProdutos:
        listagemCompleta = listaProdutos.readlines()
        ultimoElemento = len(listagemCompleta) - 1
        listaUltimoElemento = listagemCompleta[ultimoElemento].find(',')
        return listagemCompleta[ultimoElemento][0:listaUltimoElemento]

def cadastroProduto(cod, nome):
    """
    Função para cadastro do produto
    :param cod: código do produto para cadastro
    :param nome: nome do produto para cadastro
    """
    ultimoCodigo = ultimoCodigoProdutoCadastrado()
    if cod <= ultimoCodigoProdutoCadastrado():
        print(f'Coloque um código maior do que {ultimoCodigoProdutoCadastrado()}')
    else:
        with open('cadastroProduto.txt', 'a') as cadastroProduto:
            cadastroProduto.write('\n')
            cadastroProduto.write(cod)
            cadastroProduto.write(',')
            cadastroProduto.write(nome)