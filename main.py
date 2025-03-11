import func
import func.funcoes
pes = {}
while False:
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
            func.funcoes.mostra(pes)
        elif esc == 2:
            n = func.funcoes.adiciona()
        elif esc == 3:
            print('Tchau')
            break
        else:
            print('TRY AGAIN')
    except ValueError:
        print('TRY AGAIN')
