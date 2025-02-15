from utilitarios.limpar_terminal import clear
from exercicios.tuplas_e_listas import get_registros, ordenar_lista

from exercicios.validadores import (
    verificar_aprovacao, verificar_elegibilidade, 
    validar_dados_processados, validar_senha_cofre, classificacao_das_notas)

from utilitarios.menu import menu_inicial

print("<div> \n"   
"   <h1>Bem vindo o sistema da Escola Vai na Web!</h1><br>\n"
"   <h2>Escola uma das opções do menu: </h2>\n"
"</div>\n"
)

opcao = ""

while opcao != "0":
    menu_inicial()
    opcao = input("> ")
    if opcao.isnumeric():
        match int(opcao):
            case 1:
                print("\n\nRestaurando as Regras Escolares")
                clear()
                verificar_aprovacao()
            case 2:
                print("\n\nO Sistema Eleitoral Secreto")
                clear()
                idade = int(input("Digite a idade do aluno: "))
                verificar_elegibilidade(idade)
            case 3:
                print("\n\nRecuperando o Sistema de Notas")
                clear()
                nota = float(input("Digite sua nota [0 a 100]: "))
                classificacao_das_notas(nota)
            case 4:
                print("\n\nRestaurando a Identificação de Números (Soma de 2 valores)")
                clear()
                valor_1 = float(input("Digite o primeiro valor: "))
                valor_2 = float(input("Digite o segundo valor: "))
                print(f"A soma de {valor_1} e {valor_2} é {valor_1 + valor_2}")
            case 5:
                print("\n\nRecuperando o Cofre de Segurança")
                clear()
                validar_senha_cofre()
            case 6:
                print("\n\nReforçando a Segurança e a Contagem do Sistema")
                clear()
                validar_dados_processados()
            case 7:
                print("\n\nOrganizando a Lista")
                clear()
                ordenar_lista()
            case 8:
                print("\n\nAcessando os Registros de Alunos")
                clear()
                get_registros()
            case 9:
                print("\n\nCalculando Dobro de um Número")
                clear()
                valor = input("Digite um valor: ")
                print(f"O dobro de {valor} é {int(valor) * 2}")
            case 10:
                print("\n\nContando Letras")
                clear()
                nome = str(input("Digite o nome do aluno: ")).capitalize()
                nome_sem_espacos = nome.replace(" ", "")
                print(f"O nome {nome} tem {len(nome_sem_espacos)} letras")
            case _:
                print(f"\n\n{opcao} não é uma opção valida!")
    else:
        print("\n\nOpção valida!")