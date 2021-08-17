from funcoes import formatacoes
from funcoes import cadastro

formatacoes.tituloCompleto('SISTEMA DELIVERY')
#print('')

while True: 
    print('')
    formatacoes.linhasTitulo('MENU PRINCIPAL')
    print('Escolha uma opção abaixo: ')
    print('1 - Cadastrar produto')
    print('2 - Cadastrar cliente')
    print('3 - Pedidos')
    print('4 - Sair')
    opcao = int(input('Opção: '))
    if opcao == 1:
        print('')
        formatacoes.linhasTitulo('CADASTRO DE PRODUTO')
        while True:
            print('')
            codigoProduto = input('Código do produto: ')
            nomeProduto = str(input('Nome do produto: ')).strip().upper()
            cadastro.cadastroProduto(codigoProduto, nomeProduto)
            
            formatacoes.linhaInformativo('PRODUTO CADASTRADO COM SUCESSO!')
            cadastro.ultimoCodigoProdutoCadastrado()
            print('1 - Cadastrar outro produto')
            print('2 - Voltar ao menu anterior')
            opcaoInterna = int(input('Opção: '))
            if opcaoInterna == 2:
                break
        
    elif opcao == 2:
        print('')
        formatacoes.linhasTitulo('CADASTRO DE CLIENTE')
        while True:
            print('')
            codigoCliente = str(input('Código do cliente: ')).strip()
            nomeCliente = str(input('Nome do cliente: ')).strip().upper()
            with open('cadastroCliente.txt', 'a') as cadastroCliente:
                cadastroCliente.write('\n')
                cadastroCliente.write(codigoCliente)
                cadastroCliente.write(',')
                cadastroCliente.write(nomeCliente)
                
            print('')
            print('CLIENTE CADASTRADO COM SUCESSO!')
            print('')
            print('1 - Cadastrar outro cliente')
            print('2 - Voltar ao menu anterior')
            opcaoInterna = int(input('Opção: '))
            if opcaoInterna == 2:
                break
    elif opcao == 4:
        break

formatacoes.tituloCompleto('SISTEMA ENCERRADO')
