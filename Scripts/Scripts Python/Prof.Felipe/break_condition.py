# Atividade 1:
def questao_um():
    senha_certa = ["python123"]

    for i in senha_certa:
        senha = str(input("Insita uma senha: "))

        if senha != i:
            senha = str(input("Tente novamente: "))

        if senha == i:
            print("Acesso liberado.")
            break

questao_um()

def questao_dois():
    pass

# Atividade 2:
# def questao_quatro():
#  print("Questão 1: ")
#  for i in range(1,20):
#      if i % 4 == 0:
#          continue
#      print(i)
#      print("\n")
#
# questao_quatro()
#
# def questao_cinco():
#     print("Questão 2: ")
#     for i in range(0,10):
#         if i % 2 == 0:
#             print(i)
#
#         # print(i)
#
# questao_cinco()