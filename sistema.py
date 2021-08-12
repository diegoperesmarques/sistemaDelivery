def linhasTitulo():
    print('-=' * 20)

linhasTitulo()
print(f'{"SISTEMA DELIVERY":^30}')
linhasTitulo()
print('')

while True: 
    print('')
    print(f'{"MENU PRINCIPAL":^20}')
    linhasTitulo()
    print('Escolha uma opção abaixo: ')
    print('1 - Cadastrar produto')
    print('2 - Cadastrar cliente')
    print('3 - Pedidos')
    print('4 - Sair')
    opcao = int(input('Opção: '))
    if opcao == 1:
        print('')
        linhasTitulo()
        print(f'{"CADASTRO DE PRODUTO":^20}')
        linhasTitulo()
        while True:
            print('')
            codigoProduto = input('Código do produto: ')
            nomeProduto = str(input('Nome do produto: ')).strip().upper()
            with open('cadastroProduto.txt', 'a') as cadastroProduto:
                cadastroProduto.write('\n')
                cadastroProduto.write(codigoProduto)
                cadastroProduto.write(',')
                cadastroProduto.write(nomeProduto)
            
            print('')
            print('PRODUTO CADASTRADO COM SUCESSO!')
            print('1 - Cadastrar outro produto')
            print('2 - Voltar ao menu anterior')
            opcaoInterna = int(input('Opção: '))
            if opcaoInterna == 2:
                break
        
    elif opcao == 2:
        print('')
        linhasTitulo()
        print(f'{"CADASTRO DE CLIENTE":^20}')
        linhasTitulo()
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

linhasTitulo()
print(f'{"SISTEMA ENCERRADO":^20}')
linhasTitulo()