def linhasTitulo(texto):
    tamanho = len(texto) + 8
    print(f'    {texto}    ')
    print('=' * tamanho)


def tituloCompleto(texto):
    tamanho = len(texto) + 8
    print('=' * tamanho)
    print(f'    {texto}    ')
    print('=' * tamanho)


def linhaInformativo(texto):
    tamanho = len(texto) + 8
    print('-' * tamanho)
    print(f'    {texto}    ')
    print('-' * tamanho)
