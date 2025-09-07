alunos=[]
while True:
    print("1-Cadastrar")
    print("2-Listar")
    print("3-Buscar")
    print("4-Remover")
    print("5-Sair")
    opcao=int(input("Escolha uma opção: "))

    if opcao==1:
        nome=input("Digite o nome do aluno: ")
        idade=int(input("Digite a idade: "))
        matricula=int(input("Digite o número da matrícula: "))
        aluno={"nome":nome, 
               "idade":idade, 
               "matricula":matricula}
        alunos.append(aluno)
        print("\nAluno cadastrado com sucesso!\n")

    elif opcao==2:
        if len(alunos)==0:
            print("\nNenhum aluno cadastrado\n")
        else:
            for aluno in alunos:
                print(f"\nNome: {aluno['nome']}, Idade: {aluno['idade']}, Matricula: {aluno['matricula']}\n")

    elif opcao==3:
        matricula=int(input("Digite o número da matrícula"))
        encontrado=False
        for aluno in alunos:
            if aluno['matricula']==matricula:
                print(f"\nNome: {aluno['nome']}, Idade: {aluno['idade']}, Matricula: {aluno['matricula']}\n")
                encontrado=True
                break
        if not encontrado:
                print("\nAluno não encontrado.\n")

    elif opcao==4:
        matricula=int(input("Digite a matrícula do aluno para remover:"))
        encontrado=False
        for aluno in alunos:
            if aluno['matricula']==matricula:
                alunos.remove(aluno)
                print(f"\nAluno removido com sucesso!\n")
                encontrado=True
                break
        if not encontrado:
                print("\nAluno não encontrado.\n")

    elif opcao==5:
        print("\nSaindo do programa...\n")
        break

    else:
        print("\nOpção inválida, tente novamente!\n")

