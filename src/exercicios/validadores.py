from utilitarios.limpar_terminal import clear

def verificar_aprovacao():
    print("1:  Verificar aprovação de alguns aluno")
    total = 0
    cont = 1
    for cont in range(1,5):
        valor = input(f"Digite a {cont}º nota: ")
        if valor.isnumeric:
            total += float(valor)
            cont += 1
        else:
            print(f"{valor} não é uma entrada valida.")

    media = total / cont
    
    if media >= 6:
        print(f"Nota {media}. O aluno esta APROVADO")
    else:
        print(f"Nota {media}. O aluno esta REPROVADO")
    
    continuar = str(input("Deseja verificar para outro aluno ? [SIM/NAO]"))[0].upper()
    print(continuar)
    if continuar == "S":
        clear()
        verificar_aprovacao()
    elif continuar == "N":
        pass

def verificar_elegibilidade(idade):
    
    if idade >= 16:
        print("Com essa idade o aluno podera votar")
    else:
        print(f"Ainda falta {16 - idade} anos para que ele tenha permição para votar")
  
    

def validar_senha_cofre():
    cont = 1
    while cont <= 3:
        valor_digitado = str(input("Digite a senha: "))
        if valor_digitado == "Python123":
            print("Cofre desbloqueado")
            break
        else:
            print("Senha incorreta!")
            cont += 1
    if cont > 3:
        print("Acabou suas tentativas! Contate o menino(a) da T.I")

def validar_dados_processados():
    cont = 1
    while cont <= 10:
        print(cont)
        cont += 1

def classificacao_das_notas(nota):
    if nota >= 90:
        print("Parabéns, você tirou A!")
    elif nota >= 80:
        print("Muito bem, você tirou B.")
    elif nota >= 70:
        print("Bom trabalho, você tirou C.")
    elif nota >= 60:
        print("Fique atento, você tirou D.")
    else:
        print("Estude um pouco mais, você tirou F.")   
