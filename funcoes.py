import json

def salvar_dicionarios(dicionario, nome_do_arquivo):
    with open(f'{nome_do_arquivo}.json', 'w') as file:
        json.dump(dicionario, file)
        
def pegar_dicionario(nome_do_arquivo):
    with open(f'{nome_do_arquivo}.json', 'r') as file:
        return json.load(file)

def matricula_incremental(dicionario):
    if len(dicionario) != 0:
        matricula = max(dicionario.keys())
        return int(matricula) + 1
    matricula = 0
    return matricula

def tratamento_nome(nome):
    if ' ' in nome and nome.replace(' ', '').isalpha():
        return True
    return False

def tratamento_matricula_existente(matricula, dicionario):
    if matricula in dicionario:
        return True
    return False

def cadastrar(dicionario, nome, nome_do_arquivo):
    if tratamento_nome(nome):
        dicionario[str(matricula_incremental(dicionario))] = nome
        salvar_dicionarios(dicionario, nome_do_arquivo)
        pegar_dicionario(nome_do_arquivo)
        return True
    print('\n---O nome deve ser composto e não pode conter números---')
    return False

def pesquisar_usuario(dicionario, nome, acao):
    dicionario_nomes = {}
    for matricula, nome_cadastrado in dicionario.items():
        for palvras in nome.split():
            if palvras.lower() in nome_cadastrado.lower():
                dicionario_nomes[matricula] = nome_cadastrado

    if len(dicionario_nomes) == 0:
        print('\n---Usuário não encontrado---')
        return False
    
    print(f'========= USUÁRIOS =========')
    print('=-' * 18 + '=')
    print(f"{'|Nome:':<20} {'|Matricula:':>16}")
    for matricula, nome in dicionario_nomes.items():  
            print('-'*37)
            print(f'|{nome:<24} |{matricula:>5}')
    print('=-' * 18 + '=\n')

    while True:
        matricula = input(f'\n>>> Digite a matricula que deseja {acao} ou [s] para sair: ')
        if matricula in 'sS':
            break
        else:
            if matricula in dicionario_nomes:
                return matricula
            print('\n---Matricula Inválida---')
            
    return False

def atualizar(dicionario, nome, matricula, nome_do_arquivo):
    dicionario[matricula] = nome
    print('\n---Atualizado com sucesso!---')
    salvar_dicionarios(dicionario, nome_do_arquivo)
    pegar_dicionario(nome_do_arquivo)
    return True

def ver_usuario(dicionario, tabela):
    print(f'========= {tabela:^16} =========')
    print('=-' * 18 + '=')
    print(f"{'|Nome:':<20} {'|Matricula:':>16}")
    for matricula, nome in dicionario.items():    
        print('-'*37)
        print(f'|{nome:<24} |{matricula:>5}')
    print('=-' * 18 + '=\n')

def apagar(dicionario, matricula, nome_do_arquivo):
    del dicionario[matricula]
    print('\n---Apagado com sucesso!---')
    salvar_dicionarios(dicionario, nome_do_arquivo)
    pegar_dicionario(nome_do_arquivo)

def cadastrar_turmas(dicionario, nome_da_turma, professor, alunos, nome_do_arquivo):
    novo_dicionario = {}
    for matricula, nome in professor.items():
        novo_dicionario = {
            'matricula': matricula,
            nome: alunos
        }
    dicionario[nome_da_turma] = novo_dicionario
    salvar_dicionarios(dicionario, nome_do_arquivo)
    pegar_dicionario(nome_do_arquivo)

def checar_professor(dicionario, matricula):
    lista_de_materias = []

    for materia in dicionario.keys():
        if matricula == dicionario[materia]['matricula']:
            lista_de_materias.append(materia)

    if len(lista_de_materias) == 0:
        print('\n---Esse professor não possui turmas---')
        return False
    index = 0
    print('\n-------Materias--------')
    for materias in lista_de_materias:
        print(f'{index} - {materias}')
        index += 1
    return lista_de_materias

def adicionar_aluno_na_turma(dicionario):

    while True:
        nome_usuario = input('\n>>> Digite o nome do aluno que deseja colocar ou [s] para sair: ')

        if nome_usuario in 'sS':
            break
        matricula = pesquisar_usuario(dicionario, nome_usuario, 'adicionar')

        if matricula == False:
            continue
        
        dicionario_aluno_turma = {}
        dicionario_aluno_turma[matricula] = dicionario[matricula]
        return dicionario_aluno_turma


def tratamento_apagando_professor(dicionario, matricula, nome_do_arquivo):
    lista_para_deletar = []
    for materias in dicionario.keys():
        if matricula == dicionario[materias]['matricula']:
            lista_para_deletar.append(materias)
    
    for materias in lista_para_deletar:
        del dicionario[materias]
    salvar_dicionarios(dicionario, nome_do_arquivo)
    pegar_dicionario(nome_do_arquivo)

def tratamento_atualizando_professor(dicionario_turma, dicionario_professor, matricula, novo_nome, nome_do_arquivo):
    for materias in dicionario_turma.keys():
        if matricula == dicionario_turma[materias]['matricula']:
            dicionario_turma[materias] = {
                'matricula': matricula, novo_nome: dicionario_turma[materias][dicionario_professor[matricula]].copy()
            }
        
    salvar_dicionarios(dicionario_turma, nome_do_arquivo)
    pegar_dicionario(nome_do_arquivo)

def tratamento_apagar_aluno(dicionario, matricula, nome_do_arquivo):
    for materias in dicionario.values():
        for alunos in materias.values():
            index = 0
            if type(alunos) == list:
                for nomes in alunos:
                    if matricula in nomes:
                        alunos.pop(index)
                    index += 1
    salvar_dicionarios(dicionario, nome_do_arquivo)
    pegar_dicionario(nome_do_arquivo)

def tratamento_atualizando_aluno(dicionario_turma, matricula, novo_nome, nome_do_arquivo):
    for materias in dicionario_turma.values():
        for alunos in materias.values():
            if type(alunos) == list:
                for nomes in alunos:
                    if matricula in nomes:
                        nomes[matricula] = novo_nome

    salvar_dicionarios(dicionario_turma, nome_do_arquivo)
    pegar_dicionario(nome_do_arquivo)

def ver_todas_as_turmas(dicionario):
    lista_de_materias = []
    print('\n======== MATERIAS ========')
    index = 0
    for materias in dicionario.keys():
        print(f'{index} - {materias}')
        lista_de_materias.append(materias)
        index += 1

    return lista_de_materias

def ver_turmas(dicionario):

    while True:
        lista_de_materias = []
        escolha = input("\n>>> Pesquiser por uma turma ou \n[1] Ver todas \n[s] Sair\nEscolha: ") 
        if escolha != '1' and escolha != 's':
            for materias in dicionario.keys():
                for palavras in escolha.split():
                    if palavras.title() in materias:
                        if materias not in lista_de_materias:
                            lista_de_materias.append(materias)

            if len(lista_de_materias) == 0:
                print('\n--- Materia não encontrada no sistema---')
                continue
            index = 0
            print('\n===== MATERIAS ======')
            for materias in lista_de_materias:
                print(f'{index} - {materias}')
                index += 1
            return lista_de_materias

        elif escolha == '1':
            return ver_todas_as_turmas(dicionario)
        
        elif escolha in 'sS':
            return False
            
        print('\n--- Valor invalido ----')
        continue

def deletar_turma(dicionario, materia, nome_do_arquivo):
    del dicionario[materia]
    print('\n---Materia deletada com sucesso!---')
    salvar_dicionarios(dicionario, nome_do_arquivo)
    pegar_dicionario(nome_do_arquivo)
    
def mostrar_turma(dicionario, turma_selecionada):
    print(f'\n ======= Turma de {turma_selecionada} =======')
    dicionario_turma = dicionario[turma_selecionada]
    matricula_do_professor = ''
    for professores, alunos in dicionario_turma.items():
        if professores == 'matricula':
            matricula_do_professor = alunos
        else:
            print(f'\nNome: {professores} | MATRICULA: {matricula_do_professor}')
            for dicionario_aluno in alunos:
                for matricula, nome in dicionario_aluno.items():
                    print(f'\t{nome} - {matricula}')
    print(f'\n ============================================')
        
def editar_turma(dicionario_turma, dicionario_professor, dicionario_aluno):
    lista_de_turmas = ver_turmas(dicionario_turma)
    if not lista_de_turmas:
        return True
    while True:
        turma_selecionada = input("\n>>> Insira o ID da turma que deseja editar: ")
        if not turma_selecionada.isnumeric() or '':
            print('\n-- Matrícula Inválida --')
            continue
        elif int(turma_selecionada) > len(lista_de_turmas):
            print('\n-- Matrícula Inválida --')
            continue
        pessoa_a_editar = input("Selecione que tipo de pessoa deseja alterar\n [1] - Professor\n [2] - Alunos\n [0] - Voltar\n Escolha: ")
        if pessoa_a_editar == '1':
            while True:
                nome_professor_procurar = input('\n>>> Insira o nome do professor a se pesquisar: ')
                matricula_prof_atualizar = pesquisar_usuario(dicionario_professor, nome_professor_procurar, 'atualizar')
                if matricula_prof_atualizar == False:
                    break
                dicionario_de_professores = dicionario_turma[lista_de_turmas[int(turma_selecionada)]]
                if dicionario_de_professores["matricula"] == matricula_prof_atualizar:
                    print("\n -- Este professor já esta cadastrado nesta turma! --")
                    continue
                for professor, alunos in dicionario_de_professores.items():
                    if type(alunos) == list:
                        dicionario_turma[lista_de_turmas[int(turma_selecionada)]] = {
                            "matricula": matricula_prof_atualizar, dicionario_professor[matricula_prof_atualizar]: alunos
                        }
                        print("\n-- O professor da turma foi atualizado com sucesso --")
                        return True
        elif pessoa_a_editar == '2':
            while True:
                dicionario_de_alunos = dicionario_turma[lista_de_turmas[int(turma_selecionada)]]
                for alunos in dicionario_de_alunos.values():
                    lista_de_alunos = alunos
                while True:
                    acao = input("\n>>> Insira a ação que deseja realizar: \n[1] - Adicionar \n[2] - Remover \nEscolha: ")
                    if acao == '1':
                        nome_aluno_alterar = input("\n>>> Insira o nome do aluno a se pesquisar: ")
                        matricula_aluno_atualizar = pesquisar_usuario(dicionario_aluno, nome_aluno_alterar, 'atualizar')
                        if matricula_aluno_atualizar == False:
                            break
                        dicionario_para_atualizacao = {matricula_aluno_atualizar: dicionario_aluno[matricula_aluno_atualizar]}
                        if dicionario_para_atualizacao in lista_de_alunos:
                            print("\n-- Este aluno já esta cadastrado nesta turma! --")
                            continue
                        lista_de_alunos.append(dicionario_para_atualizacao)
                        print("\n-- Aluno adicionado com sucesso! --")
                        return True
                    elif acao == '2':
                        while True:
                            nome_aluno_apagar = input("\n>>> Insira o nome do aluno a se pesquisar ou aperte [1] para ver todos: ")
                            if nome_aluno_apagar == '1':
                                for alunos in lista_de_alunos:
                                    for matricula, nome in alunos.items():
                                        print(f"{matricula} - {nome}")
                                matricula_aluno_apagar = input("\n>>> Digite a matricula do aluno a se apagar ou 's' para sair: ")
                                if matricula_aluno_apagar in 'sS':
                                    break
                                index = 0
                                for alunos in lista_de_alunos:
                                    for matricula in alunos.keys():

                                        if matricula == matricula_aluno_apagar:
                                            lista_de_alunos.pop(index)
                                            print('\n--- Aluno deletado da turma com sucesso! ---')   
                                            return True
                                    index += 1

                            matricula_do_aluno = pesquisar_usuario(dicionario_aluno, nome_aluno_apagar, 'deletar')
                            if not matricula_do_aluno:
                                break
                            index = 0
                            for alunos in lista_de_alunos:
                                for matricula in alunos.keys():

                                    if matricula == matricula_do_aluno:
                                        lista_de_alunos.pop(index)
                                        print('\n--- Aluno deletado da turma com sucesso! ---')          
                                        return True
                                index += 1

                            print('\n--- Aluno não esta cadastrado nesta materia ---')

def ver_alunos_de_uma_turma(dicionario, escolha):
    for alunos in dicionario[escolha].values():
        if type(alunos) == list:
            for alunos_da_turma in alunos:
                print(f"|{'Matricula':^20} | {'Nome':^20}|")
                print('-'*45)
                for matricula, nome in alunos_da_turma.items():
                    print(f'|{matricula:^20} | {nome:^20}|')
    return True
                                            
