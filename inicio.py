
## Chamada de ambos os arquivos '.py' que possuem as separações do código.

from menus import*
from funcoes import*

dicionario_aluno = pegar_dicionario('alunos')
dicionario_professor = pegar_dicionario('professores')
dicionario_turma = pegar_dicionario('turmas')

## Variáveis compativeis com erros:

ausencia_cadastro_professores = '\n -- Você não possui professores cadastrados!, Ou eles foram apagados, Tente criar um! --'
ausencia_cadastro_alunos = '\n -- Você não possui alunos cadastrados!, Ou eles foram apagados!, Tente criar um! --'
ausencia_cadastro_turmas = '\n -- Você não possui turmas cadastradas!, Ou elas foram apagadas!, Tente criar uma! --'

## Loop principal sobre a escolha de menus.
while True:
    
    ## Seleção de escolha do menu principal.
    escolha = menu_principal()
    
    ## Entrada no menu de Coordenador.
    if escolha == '1':
        
        ## Loop de escolha no menu de Coordenador.
        while True:
            
            ## Receptor de escolha.
            escolha = menu_do_coordenador()

            if escolha == '1':
                ## Cadastro de uma turma.
                
                ## Verificadores de integridade.
                if len(dicionario_aluno) == 0:
                    print("\n -- Não existem alunos cadastrados!, Tente criar um --")
                    continue
                adicionar_turma = True
                if len(dicionario_professor) == 0:
                    print('\n--- Sem professores cadastrados não é possível criar uma turma ---')
                    continue              
                
                ## Loop da função de inserção de turmas.
                while adicionar_turma:
                    lista_aluno = []
                    dicionario_professor_turma = {}
                    nome = input('\n>>> Digite o nome da turma que deseja adicionar ou [s] para sair: ').title()

                    ## Possível saída.
                    if nome in 'sS':
                        break
                    
                    ## Corretor de nomes de turmas iguais.
                    if nome in dicionario_turma:
                        print('\n--- Turma já existente ---')
                        continue

                    procurar_professor = True
                    
                    ## Loop para cadastro de professor na turma.
                    while procurar_professor:
                        nome_usuario = input('\n>>> Digite o nome do professor que deseja colocar ou [s] para sair: ')

                        ## Possível saída.
                        if nome_usuario in 'sS':
                            break

                        matricula = pesquisar_usuario(dicionario_professor, nome_usuario, 'adicionar')

                        if matricula == False:
                            continue
                        
                        dicionario_professor_turma[matricula] = dicionario_professor[matricula]

                        ## Loop para cadastro de alunos na turma.
                        while True:
                            dicionario_para_armazenar_alunos = adicionar_aluno_na_turma(dicionario_aluno)
                            
                            ## Verificador de existência do aluno na turma.
                            if dicionario_para_armazenar_alunos in lista_aluno:
                                print('\n--- Esse aluno já está cadastrado na turma ---')
                                continue
                            lista_aluno.append(dicionario_para_armazenar_alunos)
                            escolha = input('\n>>> Deseja adicionar outro alunos? [s]im ou [n]ão: ')
                            
                            ## Possível saída.
                            if escolha in 'sS':
                                continue

                            ## Sequência, pós inserção, com as informações para o cadastro da turma.
                            cadastrar_turmas(dicionario_turma, nome, dicionario_professor_turma, lista_aluno, 'turmas')
                            adicionar_turma = False
                            procurar_professor = False
                            break

            elif escolha == '2':
                ## Edição de uma turma.

                ## Verificador de integridade.
                if len(dicionario_turma) == 0:
                    print(ausencia_cadastro_turmas)
                else:
                    ## Chamada das funções de: "Edição Geral", e das funções de "Load Geral" do código.
                    editar_turma(dicionario_turma, dicionario_professor, dicionario_aluno)
                    salvar_dicionarios(dicionario_turma, 'turmas')
                    pegar_dicionario('turmas')

            elif escolha == '3':
                ## Visualizar turma(as).

                ## Verificador de integridade.
                if len(dicionario_turma) == 0:
                    print(ausencia_cadastro_turmas)
                else:
                    ## Chamada da função para ver uma turma específica baseada na inserção do usuário.
                    lista_de_turmas = ver_turma_especifica(dicionario_turma)
                    if not lista_de_turmas:
                        break
                    
                    ## Loop para pesquisa de turmas.
                    while True:
                        turma_a_selecionar = input("\n>>> Selecione a turma na qual você deseja ver ou 's' para sair: ")
                        
                        ## Possível saída.
                        if turma_a_selecionar in 'sS':
                            break

                        ## Receptor de inserção, que recebe o inserido, e trabalha a partir dele na procura de turmas correspondentes, em busca "ID"
                        elif turma_a_selecionar.isnumeric():
                            if int(turma_a_selecionar) <= len(lista_de_turmas):
                                mostrar_turma(dicionario_turma, lista_de_turmas[int(turma_a_selecionar)])
                            
            elif escolha == '4':
                ## Apagar determinada turma.

                ## Verificador de integridade.
                if len(dicionario_turma) == 0:
                    print(ausencia_cadastro_turmas)
                else:
                    lista_de_turmas = ver_turma_especifica(dicionario_turma)

                    if not lista_de_turmas:
                        break
                    
                    ## Loop para inserção de turma a apagar.
                    while True:
                        escolha = input('\n>>> Escolha uma turma para apagar: ')
                        if escolha.isnumeric():
                            if int(escolha) <= len(lista_de_turmas):
                                ## Chamada da função que deve deletar a turma inserida.
                                deletar_turma(dicionario_turma, lista_de_turmas[int(escolha)], 'turmas')
                                break
                        print('\n--- Escolha Inválida ---')
                        continue

            elif escolha == '0':
                ## Saída principal do código.
                break

            ## Possível erro de ausência de existência de uma escolha.
            else:
                print('\n--- Escolha Inválida ---')
    
    elif escolha == '2':
        ## Entrada no menu de Professores.
        
        ## Loop de escolha no menu de Professores.
        while True:
            
            ## Receptor de escolha.
            escolha = menu_de_professores()

            if escolha == '1':
                ## Cadastro de um novo professor.

                ## Loop para inserção do nome do professor.
                while True:
                    nome = input('\n>>> Digite um nome para cadastrar ou "s" para sair: ')
                    if nome in 'sS':
                        break
                    ## Verificação de regimentos do nome do professor a partir da função.
                    if cadastrar(dicionario_professor, nome, 'professores'):
                        print('\n--- Cadastro Efetuado ---')
                        break
                    
            elif escolha == '2':
                ## Edição de um professor.

                ## Verificador de erro.
                if len(dicionario_professor) == 0:
                    print(ausencia_cadastro_professores)
                else:
                    atualizar_loop = True
                    
                    ## Loop para inserção do nome do professor para procura e edição.
                    while atualizar_loop:
                        nome = input('\n>>> Digite o nome que deseja pesquisar ou [s] para sair: ')
                        
                        ## Possível saída.
                        if nome in 'sS':
                            break
                        else:
                            ## Coleta da matrícula do professor a atualizar, a partir da função de "Pesquisa Geral"
                            matricula = pesquisar_usuario(dicionario_professor, nome, 'atualizar')
                            
                            if not matricula:
                                continue

                            ## Loop para nova inserção/atualização do professor seleiconado.
                            while True:
                                nome = input('\n>>> Digite o novo nome que deseja colocar: ')
                                
                                ## Atualização do nome do professor fora e dentro de turmas.
                                if tratamento_nome(nome):
                                    tratamento_atualizando_professor(dicionario_turma, dicionario_professor, matricula, nome, 'turmas')
                                    atualizar(dicionario_professor, nome, matricula, 'professores')
                                    atualizar_loop = False
                                    break

                                ## Possível erro de integridade.    
                                print('\n--- O nome deve ser composto e não pode conter números ---')  
                                continue

            elif escolha == '3':
                ## Ver professores cadastrados.
                
                ## Verificador de erro.
                if len(dicionario_professor) == 0:
                    print(ausencia_cadastro_professores)
                else:
                    ## Chamada da função que, pós inserção, co-relaciona o nome do professor inserido com os existentes para seleção por "ID".
                    ver_usuario(dicionario_professor, 'Professores')

            elif escolha == '4':
                ## Excluir um professor.

                ## Verificador de erro.
                if len(dicionario_professor) == 0:
                    print(ausencia_cadastro_professores)
                else:
                    
                    ## Loop para inserção do professor a apagar.
                    while True:
                        nome = input('\n>>> Digite o nome que deseja pesquisar ou [s] para sair: ')
                        
                        ## Possível saída.
                        if nome in 'sS':
                            break
                        else:
                            ## Coleta da matrícula do professor a apagar, a partir da função de "Pesquisa Geral"
                            matricula = pesquisar_usuario(dicionario_professor, nome, 'apagar')
                            if not matricula:
                                continue
                            ## Chamada das funções que apagam um professor do dicionário principal, dentro e fora de turmas.
                            apagar(dicionario_professor, matricula, 'professores' )
                            tratamento_apagando_professor(dicionario_turma, matricula, 'turmas')
                            break
            
            elif escolha == '5':
                ## Visualizar as turmas de um professor.
                
                ## Verificador de erro.
                if len(dicionario_professor) == 0:
                    print(ausencia_cadastro_professores)
                else:
                    ## Loop para inserção de um professor a se ver as turmas.
                    while True:
                        nome = input('\n>>> Digite o nome do professor que deseja ver as turmas ou [s] para sair: ')
                        
                        ## Possível saída.
                        if nome in 'sS':
                            break

                        ## Coleta da matrícula do professor a se pesquisar, a partir da função de "Pesquisa Geral"
                        matricula = pesquisar_usuario(dicionario_professor, nome, 'ver')

                        if matricula == False:
                            continue   
                            
                        ## Verificador da existência de um professor em turmas ou não, seguido de chamada.
                        checar_turmas_de_um_professor(dicionario_turma, matricula)

            elif escolha == '6':
                ## Visualizar os alunos de uma turma específica de um professor.
                
                ## Verificador de erro.
                if len(dicionario_professor) == 0:
                    print(ausencia_cadastro_professores)

                else:
                    
                    ## Loop para inserção do professor a se explorar as turmas.
                    while True:
                        nome = input('\n>>> Digite o nome do professor que deseja ver as turmas ou [s] para sair: ')
                        
                        ## Possível saída.
                        if nome in 'sS':
                            break
                        
                        ## Coleta da matrícula do professor a pesquisar, a partir da função de "Pesquisa Geral"
                        matricula = pesquisar_usuario(dicionario_professor, nome, 'ver')

                        if matricula == False:
                            continue
                        
                        ## Verificador da existência de um professor na matéria selecionada.
                        lista_de_materias =  checar_turmas_de_um_professor(dicionario_turma, matricula)
                        if not lista_de_materias:
                            continue
                        
                        ## Loop de escolha da matéria do professor(listadas) a se ver os alunos.
                        while True:
                            escolha = input('\n>>> Escolha uma máteria para ver os alunos: ')
                            
                            ## Verificador de integridade de escolha.
                            if int(escolha) > len(lista_de_materias) or not escolha.isnumeric():
                                print('\n--- Valor inválido ---')
                                continue
                            
                            ## Chamada da função que exibe os alunos da específica turma selecionada.
                            if ver_alunos_de_uma_turma(dicionario_turma, lista_de_materias[int(escolha)]):
                                break
            
            elif escolha == '0':
                ## Saída do menu de professores e volta ao código principal.
                break

    elif escolha == '3':
        ## Entrada no menu de Alunos.
        
        ## Loop de escolha no menu de Alunos
        while True:
            
            ## Receptor de escolha.
            escolha = menu_de_alunos()

            if escolha == '1':
                ## Cadastrando um aluno.
                
                ## Loop de inserção do nome do aluno 
                while True:
                    nome = input('\n>>> Digite um nome para cadastrar ou "s" para sair: ')
                    if nome in 'sS':
                        break
                    resultado = cadastrar(dicionario_aluno, nome, 'alunos')
                    if resultado:
                        print('\n--- Cadastro Efetuado ---')
                        break
            
            elif escolha == '2':
                if len(dicionario_aluno) == 0:
                    print(ausencia_cadastro_professores)
                else:
                    atualizar_loop = True
                    while atualizar_loop:
                        nome = input('\n>>> Digite o nome que deseja pesquisar ou [s] para sair: ')
                        if nome in 'sS':
                            break
                        else:
                            matricula = pesquisar_usuario(dicionario_aluno, nome, 'atualizar')

                            if not matricula:
                                continue

                            while True:
                                nome = input('\n>>> Digite o novo nome que deseja colocar: ')
                                if tratamento_nome(nome):
                                    tratamento_atualizando_aluno(dicionario_turma, matricula, nome, 'turmas')
                                    atualizar(dicionario_aluno, nome, matricula, 'alunos')
                                    atualizar_loop = False
                                    break
                                    
                                print('\n--- O nome deve ser composto e não pode conter números ---')  
                                continue

            elif escolha == '3':
                if len(dicionario_aluno) == 0:
                    print(ausencia_cadastro_alunos)
                else:
                    ver_usuario(dicionario_aluno, 'Alunos')
            
            elif escolha == '4':
                if len(dicionario_aluno) == 0:
                    print(ausencia_cadastro_alunos)
                else:
                    while True:
                        nome = input('\n>>> Digite o nome que deseja pesquisar ou [s] para sair: ')
                        if nome in 'sS':
                            break
                        else:
                            matricula = pesquisar_usuario(dicionario_aluno, nome, 'apagar')

                            if matricula == False:
                                continue
                            apagar(dicionario_aluno, matricula, 'alunos' )
                            tratamento_apagar_aluno(dicionario_turma, matricula, 'turmas')
                            break

            elif escolha == '0':
                break
    
    elif escolha == '0':
        print('\n---Programa encerrado---')
        break

    else:
        print('\n---Escolha Inválida---')
