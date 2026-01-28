tarefas = []

while True:
    print('\n=== GERENCIADOR DE TAREFAS ===')
    print('[1] Adicionar tarefa')
    print('[2] Listar tarefas')
    print('[3] Remover tarefa')
    print('[4] Concluir tarefa (EM DESEMVOLCIMENTO)')
    print('[0] Sair')

    escolha = int(input('Selecione uma opção: '))

    if escolha == 0:
        print('Saindo do organizador de tarefas...')
        print('Você saiu do organizador.')
        break

    elif escolha == 1:
        print('\n[ADICIONAR TAREFA]')
        tarefa = input('Digite a tarefa: ')
        tarefas.append(tarefa)
        print('Tarefa adicionada com sucesso!')

    elif escolha == 2:
        print('\n[LISTA DE TAREFAS]')
        if not tarefas:
            print('Sem tarefas.')
        else:
            for tarefa in tarefas:
                print('-', tarefa)

    elif escolha == 3:
        print('\n[REMOVER TAREFA]')
        if not tarefas:
            print('Sem tarefas para remover.')
        else:
            for tarefa in tarefas:
                print('-', tarefa)

            opcao = input('Digite o nome da tarefa que deseja remover: ')
            if opcao not in tarefas:
                print('Tarefa não existe.')
            else:
                tarefas.remove(opcao)
                print('Tarefa removida com sucesso.')

   

        
        
            

        
        

    

