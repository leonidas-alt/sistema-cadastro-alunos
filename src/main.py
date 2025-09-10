alunos=[]
def cadastrar():
    global gera_matricula
    print("Digite")
    matricula=gera_matricula
    gera_matricula+=1

def listar():
    if not alunos:

        return
def buscar():
    for aluno in alunos:
        if aluno ["..."]==matricula:

            return
def atualizar():
    matricula=int(input("..."))
    for aluno in alunos:
        if aluno["..."]==matricula:
            print("O que deseja atualizar?")

            opcao=input("Escolha: ")
        if opcao == "1":
            aluno["nome"]= input("Novo nome: ")
        elif opcao == "2":
            aluno["idade"]= input("Nova idade: ")
        else: 
            print("Opção inválida!")

            return
        print("sucesso!")
        return 
def remover():
    matricula=input("Digite o nome do aluno: ")
    encontrado=False
    for aluno in alunos:
        if aluno['matricula']==matricula:
            alunos.remove(alunos)
            print("Aluno removido com sucesso!")
            encontrado=True
            break
        if not encontrado: 
            print("Aluno não encontrado.")
while True:
    print("...")
    opcao=input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar()
    if opcao == "2":
        listar()
    if opcao == "3":
        buscar()
    if opcao == "4":
        atualizar()
    if opcao == "5":
        remover()
    if opcao == "6":
        print("Saindo...")
        break
    else:
        print("Opção inválida, tente novamente!")
                        

