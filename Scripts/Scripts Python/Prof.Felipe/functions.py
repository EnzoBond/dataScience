def media_nota():
    print("Questão 1: ")
    nome = str(input("Digite o nome do aluno: "))
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3

    if media >= 7.0:
        print(f"O aluno {nome} foi aprovado com sucesso: {media}")
    elif media < 7.0:
        print(f"O aluno {nome} ficou de recuperação com a media: {media}")
    elif media < 5.0:
        print(f"O aluno {nome} foi reprovado com a media: {media}")

media_nota()

def calcular_media(nota1, nota2, nota3):
    print("Questão 2: ")
    media = (nota1 + nota2 + nota3) / 3
    return media

def verificar_situacao(
    media = float(input("Digite a media do aluno: "))):
    print("Questão 3: ")
    if media >= 7.0:
        print(f"Aprovado com sucesso: {media}")
    elif media < 7.0:
        print(f"Recuperação com a media: {media}")
    elif media < 5.0:
        print(f"Reprovado com a media: {media}")

verificar_situacao()

def executar():
    print("Questão 4: ")
    nome = str(input("Digite o nome do aluno: "))
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = calcular_media(nota1, nota2, nota3)

    if media >= 7.0:
        print(f"Aluno: {nome} \n")
        print(f"Media: {media} \n")
        print("Situação: Aprovado.")

    elif media < 7.0:
        print(f"Aluno: {nome} \n")
        print(f"Media: {media} \n")
        print("Situação: Recuperação.")

    elif media < 5.0:
        print(f"Aluno: {nome} \n")
        print(f"Media: {media} \n")
        print("Situação: Reprovado.")

executar()

def calcular_imc():
    print("Questão 5: ")
    nome = str(input("Digite o nome do aluno: "))
    peso = float(input("Digite o peso do aluno: "))
    altura = float(input("Digite a altura do aluno: "))

    imc = peso / (altura ** 2)

    if imc < 18.5:
        print(f"Aluno: {nome} \n")
        print(f"IMC: {imc} \n")
        print("Situação: Abaixo do peso.")

    elif imc >= 18.5 and imc <= 24.9:
        print(f"Aluno: {nome} \n")
        print(f"IMC: {imc} \n")
        print("Situação: Peso normal.")

    elif imc >= 25.0 and imc <= 29.9:
        print(f"Aluno: {nome} \n")
        print(f"IMC: {imc} \n")
        print("Situação: Sobrepeso.")

    else:
        print(f"Aluno: {nome} \n")
        print(f"IMC: {imc} \n")
        print("Situação: Obesidade.")

calcular_imc()

def somar():
    print("Questão 6: ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    print(f"A soma dos dois números é: {num1 + num2}")