tarefas = []

while True:
    print('[1] Adicionar tarefa.')
    print('[2] Listar tarefas.')
    print('[3] Remover tarefa.')
    print('[0] Sair.')

    escolha = int(input('Selecione uma opção:'))

    if escolha == 0:
        print('Saindo do organizador de tarefas.')
        print('Você saiu do organizador.')
        break
    
    elif escolha == 1:
        print('[ADICIONAR TAREFAS]')
        tarefa = input('Adicionar tarefa:')
        tarefas.append(tarefa)

        print('Tarefa Adicionada com Sucesso:')
        print(tarefas)

    elif escolha == 2:
        print('[LISTA DE TAREFAS]')
        if not tarefas:
            print('Sem tarefas')
        else:
            for tarefa in tarefas:
                print(tarefa)

    tarefas = []

while True:
    print('[1] Adicionar tarefa.')
    print('[2] Listar tarefas.')
    print('[3] Remover tarefa.')
    print('[4] Concluir tarefa.')
    print('[0] Sair.')

    escolha = int(input('Selecione uma opção:'))

    if escolha == 0:
        print('Saindo do organizador de tarefas.')
        print('Você saiu do organizador.')
        break
    
    elif escolha == 1:
        print('[ADICIONAR TAREFAS]')
        tarefa = input('Adicionar tarefa:')
        tarefas.append(tarefa)

        print('Tarefa Adicionada com Sucesso:')
        print(tarefas)

    elif escolha == 2:
        print('[LISTA DE TAREFAS]')
        if not tarefas:
            print('Sem tarefas')
        else:
            for tarefa in tarefas:
                print(tarefa)

    elif escolha == 3:
    print('[REMOVER TAREFA]')

    if not tarefas:
        print('Sem tarefas para remover.')
    else:
        for tarefa in tarefas:
            print(tarefa)

        opcao = input('Digite o nome da tarefa: ')
        if opcao not in tarefas:
            print('Tarefa não existe.')
        else:
            tarefas.remove(opcao)
            print('Tarefa removida com sucesso.')

        
        
            

        
        

    
