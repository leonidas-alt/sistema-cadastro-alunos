# Sistema de Cadastro de Alunos

Este é um projeto simples de um **Sistema de Cadastro de Alunos** desenvolvido em Python. Ele permite realizar operações básicas de gerenciamento de alunos, como cadastrar, listar, buscar, remover e sair do programa.

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

1. **Cadastrar Aluno**: Permite adicionar um novo aluno ao sistema, informando nome, idade e número de matrícula.
2. **Listar Alunos**: Exibe todos os alunos cadastrados no sistema.
3. **Buscar Aluno**: Permite buscar um aluno pelo número de matrícula.
4. **Remover Aluno**: Remove um aluno do sistema pelo número de matrícula.
5. **Sair**: Encerra o programa.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

```
sistema-cadastro-alunos/
├── .gitignore
├── LICENSE
├── README.md
└── src/
    └── main.py
```

Os principais arquivos e diretórios do projeto são:

- **`src/main.py`**: Contém o código principal do sistema.
- **`.gitignore`**: Define os arquivos e diretórios que devem ser ignorados pelo Git.
- **`LICENSE`**: Licença do projeto (MIT License).
- **`README.md`**: Arquivo de documentação do projeto.

## Construção do Projeto

### Passo 1: Configuração do Ambiente

Certifique-se de ter o Python instalado em sua máquina. Você pode baixá-lo no site oficial: [https://www.python.org/](https://www.python.org/).

### Passo 2: Estrutura Inicial

1. Crie a estrutura de diretórios e arquivos conforme mostrado acima.
2. Adicione o arquivo `.gitignore` para ignorar arquivos desnecessários no controle de versão.

### Passo 3: Implementação do Código

O código principal foi implementado no arquivo `src/main.py`. Ele utiliza uma lista para armazenar os dados dos alunos e oferece um menu interativo para o usuário realizar as operações.

### Passo 4: Licença

O projeto foi licenciado sob a **MIT License**, permitindo o uso, modificação e distribuição do código.

## Como Executar o Projeto

1. Navegue até o diretório `src` no terminal:

   ```bash
   cd src
   ```
2. Execute o arquivo main.py com o Python:
   ```bash
   python main.py
   ```

Siga as instruções exibidas no menu interativo.

## Exemplo de Uso

### Menu Inicial

Ao executar o programa, o seguinte menu será exibido:

```
1-Cadastrar
2-Listar
3-Buscar
4-Remover
5-Sair
Escolha uma opção:
```
Cadastro de Aluno
Informe os dados do aluno, como nome, idade e matrícula. O sistema confirmará o cadastro com a mensagem:

```
Aluno cadastrado com sucesso!
```
Listagem de Alunos
Caso existam alunos cadastrados, o sistema exibirá os dados de cada aluno. Caso contrário, exibirá:

```
Nenhum aluno cadastrado
```
Busca e Remoção
O sistema permite buscar ou remover alunos pelo número de matrícula. Caso o aluno não seja encontrado, será exibida a mensagem:

```
Aluno não encontrado.
```
Saída
Para sair do programa, escolha a opção 5. O sistema exibirá:

```
Saindo do programa...
```
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

Licença
Este projeto está licenciado sob a MIT License.

Esse [README.md] fornece uma explicação detalhada sobre o projeto, incluindo funcionalidades, estrutura, passos para execução
