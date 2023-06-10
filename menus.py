# menu principal
def menu_principal():
    print('=-' * 12 + '=')
    print(' --- Menu Principal ---')
    print('[1] - Coordenador\n[2] - Professores\n[3] - Alunos\n[0] - Sair.')
    print('=-' * 12 + '=')
    return input('\n>>> Selecione uma opção: ')

# menu do coordenador
def menu_do_coordenador():
    print('=-' * 12 + '=')
    print(' --- Menu Coordenador ---')
    print('[1] - Criar Turma\n[2] - Editar Turma\n[3] - Ver Turma\n[4] - Apagar Turma\n[0] - Voltar ao menu P.')
    print('=-' * 12 + '=')
    return input('\n>>> Selecione uma opção: ')

# menu de professores
def menu_de_professores():
    print('=-' * 23 + '=')
    print('--------------- Menu Professor ----------------')
    print('[1] - Cadastrar novo Professor\n[2] - Editar Professor\n[3] - Ver dados do Professor\n[4] - Excluir professor\n[5] - Visualizar turmas do Professor\n[6] - Visualizar alunos da Turma por Professor\n[0] - Voltar ao menu P.')
    print('=-' * 23 + '=')
    return input('\n>>> Selecione uma opção: ')

# menu de alunos
def menu_de_alunos():
    print('=-' * 13 + '=')
    print('------- Menu Alunos -------')
    print('[1] - Cadastrar novo aluno\n[2] - Editar aluno\n[3] - Visualizar alunos\n[4] - Apagar alunos\n[0] - Voltar ao menu P.')
    print('=-' * 13 + '=')
    return input('\n>>> Selecione uma opção: ')