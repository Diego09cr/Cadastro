def mostra(x):
    print('-'*50)
    print(f'{"PESSOAS CADASTRADAS":^50}')
    print('-'*50)
    for i in x:
        print(f"{i:^50}")
    print('-'*50)
    return


def adiciona():
    pessoa = dict()
    print('-'*50)
    print(f'{"NOVO CADASTRO":^50}')
    print('-'*50)
    nome = str(input('Nome: '))
    pessoa["nome"] = nome
    idade = int(input('Idade: '))
    pessoa["idade"] = idade
    print(f'Novo registro de {nome} foi adicionado')
    return pessoa

def comeca():
    pes = {}
    while True:
        try:
            print('-'*50)
            print(f'{"MENU PRINCIPAL":^50}')
            print('-'*50)
            print('1 - Ver pessoas cadastradas')
            print('2 - Cadastrar nova pessoa')
            print('3 - Sair do Sistema')
            print('-'*50)
            esc = int(input('Sua opção: '))
            if esc == 1:
                mostra(pes)
            elif esc == 2:
                adiciona()
            elif esc == 3:
                print('Tchau')
                break
            else:
                print('TRY AGAIN')
        except ValueError:
            print('TRY AGAIN')