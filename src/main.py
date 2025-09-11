alunos=[]
gera_matricula=1

def cadastrar(nome, idade, matricula):
    global gera_matricula
    aluno = {
        "nome": nome,
        "idade": idade,
        "matricula": matricula
    }
    alunos.append(aluno)
    print(f"Aluno{nome} cadastrado com sucessso! Matrícula: {gera_matricula}")
    gera_matricula+=1
def listar(nome,idade,matricula):
    if not alunos:
        print("Aluno não encontrado!")
        for aluno in alunos:
            print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Matrícula: {aluno['matricula']}")
def buscar(matricula):
    for aluno in alunos:
        if aluno ['matricula']==matricula:
            print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Matrícula: {aluno['matricula']}")
            return aluno
    print("Aluno não encontrado!")
    return None
def atualizar(matricula, novo_nome=None, nova_idade=None):
    for aluno in alunos:
        if aluno['matricula']==matricula:
            if novo_nome:
                aluno['nome']=novo_nome
            if nova_idade:
                aluno['idade']=nova_idade
            print("Aluno {matricula} atualizado com sucesso!")
            return
    print("Aluno não encontrado para atualização.")
def remover(matricula):
    for aluno in alunos:
        if aluno['matricula']==matricula:
            alunos.remove(alunos)
            print(f"Aluno {aluno['nome']} removido com sucesso!")
            return 
        print("Aluno não encontrado.")
while True:
    print("\nMenu:")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno")
    print("4 - Atualizar aluno")
    print("5 - Remover aluno")
    print("6 - Sair")
    opcao=input("Escolha uma opção: ")

    if opcao == "1":
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            cadastrar(nome, idade, gera_matricula)
    elif opcao == "2":
            listar()
    elif opcao == "3":
            matricula = int(input("Matrícula do aluno: "))
            buscar(matricula)
    elif opcao == "4":
            matricula = int(input("Matrícula do aluno: "))
            novo_nome = input("Novo nome (deixe vazio para não alterar): ")
            nova_idade_str = input("Nova idade (deixe vazio para não alterar): ")
            nova_idade = int(nova_idade_str) if nova_idade_str else None
            atualizar(matricula, novo_nome if novo_nome else None, nova_idade)
    elif opcao == "5":
            matricula = int(input("Matrícula do aluno: "))
            remover(matricula)
    elif opcao == "6":
            print("Saindo...")
            break
else:
    print("Opção inválida, tente novamente!")
                        

