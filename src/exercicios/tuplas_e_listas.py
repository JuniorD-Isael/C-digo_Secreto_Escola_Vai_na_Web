alunos = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")
numeros = [8,3,10,1,5]

def get_registros():
    print(f"Primeiro aluno: {alunos[0]}\n"
          f"Ultimo aluno: {alunos[-1]}")

def ordenar_lista():
    print(f"Lista não ordenada: {numeros} \n")
    numeros.sort()
    print(f"Lista ordenada: {numeros}")