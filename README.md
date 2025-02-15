# Documentação do Projeto: **Código Secreto da Escola Vai na Web**

Este é um sistema interativo desenvolvido para o **Desafio 1: O Código Secreto da Escola Vai na Web**, projetado para realizar diversas tarefas, como verificar a aprovação de alunos, calcular notas, verificar a elegibilidade para votar e outras funcionalidades relacionadas à gestão escolar. Abaixo está a descrição dos arquivos e funcionalidades principais deste projeto.

## Estrutura do Projeto

O projeto está organizado nas seguintes pastas e arquivos:

```
src/
│
├── exercicios/
│   ├── tuplas_listas.py
│   └── validadores.py
│
├── utilitarios/
│   ├── limpar_terminal.py
│   └── menu.py
│
├── main.py
```

### Pasta `exercicios/`

- **`tuplas_listas.py`**: Contém funções para exibir e manipular listas e tuplas.
- **`validadores.py`**: Contém funções para validar diferentes entradas e verificar aprovações e elegibilidade de alunos.

### Pasta `utilitarios/`

- **`limpar_terminal.py`**: Função para limpar o terminal entre as interações do usuário.
- **`menu.py`**: Contém o menu de opções interativas do sistema.

### Arquivo `main.py`

O arquivo principal do projeto que importa e chama as funções de todos os módulos e organiza a interação com o usuário através de um menu.

---

## Descrição das Funcionalidades

### 1. **Tuplas e Listas**
Arquivo: `exercicios/tuplas_listas.py`

#### Função: `get_registros()`

Exibe o primeiro e o último aluno da lista de alunos.

```python
alunos = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")
```

Exemplo de saída:

```
Primeiro aluno: Ana
Último aluno: Eduardo
```

#### Função: `ordenar_lista()`

Ordena uma lista de números de forma crescente e exibe antes e depois da ordenação.

```python
numeros = [8, 3, 10, 1, 5]
```

Exemplo de saída:

```
Lista não ordenada: [8, 3, 10, 1, 5]
Lista ordenada: [1, 3, 5, 8, 10]
```

---

### 2. **Validadores**
Arquivo: `exercicios/validadores.py`

#### Função: `verificar_aprovacao()`

Solicita as notas de um aluno e calcula sua média. Dependendo da média, o aluno será aprovado (nota >= 6) ou reprovado.

#### Função: `verificar_elegibilidade(idade)`

Verifica se o aluno tem idade suficiente (maior ou igual a 16 anos) para votar.

#### Função: `validar_senha_cofre()`

Solicita a senha para desbloquear o cofre da escola. O usuário tem três tentativas.

#### Função: `validar_dados_processados()`

Imprime os números de 1 a 10 para garantir que os dados foram processados corretamente.

#### Função: `classificacao_das_notas(nota)`

Classifica o aluno conforme sua nota (A, B, C, D ou F).

---

### 3. **Utilitários**
Arquivo: `utilitarios/limpar_terminal.py`

#### Função: `clear()`

Limpa o terminal, dando uma sensação de "reinício" da aplicação após cada ação do usuário. A função utiliza a biblioteca `os` para detectar o sistema operacional e executar o comando adequado (no Windows ou Unix).

---

Arquivo: `utilitarios/menu.py`

#### Função: `menu_inicial()`

Exibe o menu principal do sistema, permitindo que o usuário escolha uma das opções disponíveis para realizar uma ação.

---

### 4. **Arquivo Principal (`main.py`)**

O `main.py` é o arquivo central que coordena a execução do sistema. Ele importa as funções dos módulos e exibe um menu para o usuário.

#### Fluxo de Execução:

- O programa exibe uma saudação inicial e o menu de opções.
- O usuário escolhe uma opção e o programa chama a função correspondente.
- O menu contém as seguintes opções:
    1. Verificar aprovação de um aluno.
    2. Verificar elegibilidade para votar.
    3. Classificação das provas.
    4. Somar dois valores.
    5. Validar a senha do cofre da escola.
    6. Verificar dados processados.
    7. Organizar lista de números.
    8. Acessar registros dos alunos.
    9. Calcular o dobro de um número.
    10. Contar o número de letras no nome de um aluno.
    0. Encerrar o programa.

## Como Executar

1. Clone este repositório para sua máquina local.
2. Navegue até a pasta do projeto e execute o arquivo `main.py`.
3. O menu será exibido e você pode escolher a opção que deseja executar.
4. Interaja com o sistema conforme solicitado.
