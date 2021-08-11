def linhasTitulo():
    print('-=' * 20)

linhasTitulo()
print(f'{"SISTEMA DELIVERY":^30}')
linhasTitulo()

while True: 
    print('Escolha uma opção abaixo: ')
    print('1 - Cadastrar produto')
    print('2 - Cadastrar cliente')
    print('3 - Pedidos')
    print('4 - Sair')
    opcao = int(input('Opção: '))
    if opcao == 4:
        break

linhasTitulo()
print(f'{"SISTEMA ENCERRADO":^20}')
linhasTitulo()