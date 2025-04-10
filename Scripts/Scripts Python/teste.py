print("Questão 4:")
senha = "cofre2025"
input_usuario = str(input("Digite uma senha para continuar: "))

while input_usuario != senha:
     print("Senha incorreta.")
     input_usuario = str(input("Tente novamente: "))

print("Senha correta. \n")
