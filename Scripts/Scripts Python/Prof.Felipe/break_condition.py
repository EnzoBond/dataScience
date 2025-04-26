import random as rand

# Atividade 1:
def questao_um():
    print("Questão 1: ")
    senha_certa = "python123"
    
    while True:
        senha = input("Digite a senha: ")
        if senha == senha_certa:
            print("Acesso liberado!")
            break         
        else:
            print("Senha incorreta! Tente novamente.")
            continue

questao_um()

def questao_dois():
    print("Questão 2: ")
    while True:
     numero_usuario = int(input("Adivinha um número entre 1 a 10: "))
     numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
     numero_correto = rand.choice(numeros)
    
     if numero_usuario == numero_correto:
         print("Parabéns! Você acertou o número.")
         break

questao_dois()

def questao_tres():
    for i in range(1, 100):
        if i % 13 == 0:
            break
        print(i)

questao_tres()

# Atividade 2:
def questao_quatro():
 print("Questão 4: ")
 for i in range(1,20):
     if i % 4 == 0:
         continue
     print(i)
     print("\n")

questao_quatro()

def questao_cinco():
    print("Questão 5: ")
    for i in range(0,10):
        if i % 2 == 0:
            print(i)

questao_cinco()