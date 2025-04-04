import random

def questao_1():
    print("Questão 1: ")
    contagem = 10

    while contagem != -1:
        print(contagem)
        contagem -= 1

    print("Fim da contagem. \n")

questao_1()

def questao_2():
    print("Questão 2:")
    numero = -2

    while numero != 20:
        numero += 2
        print(numero)
    print("Fim da contagem. \n")

questao_2()

def questao_3():
    print("Questão 3: ")
    numero = 0
    soma = 0

    while numero != -5:
        numero = int(input("Digite um numero abaixo de 0: "))
        if numero != -5:
            soma += numero
            print(soma)

    print("Fim do calculo. \n")

questao_3()

def questao_4():
    print("Questão 4:")
    senha = "cofre2025"
    input_usuario = str(input("Digite uma senha para continuar: "))

    while input_usuario != senha:
        print("Senha incorreta.")
        input_usuario = str(input("Tente novamente: "))

    print("Senha correta. \n")

questao_4()

def questao_5():
   print("Questão 5: ")

   while True:
       player_1 = random.randint(1, 6)
       player_2 = random.randint(1, 6)

       print(f"Player 1: {player_1}")
       print(f"Player 2: {player_2} \n")

       if player_1 > player_2:
           print("Player 1 venceu!")
           break
       elif player_1 < player_2:
           print("Player 2 venceu!")
           break

questao_5()