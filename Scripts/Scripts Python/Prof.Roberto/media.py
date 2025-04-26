nota1 = float(input("Insira nota 1: "))
nota2 = float(input("Insira nota 2: "))

def calculo_media():
    print(nota1 + nota2)
    media_final = (nota1 + nota2) / 2

    if media_final >= 7.0:
        print(f"Aprovado com sucesso: {media_final}")
    else:
        print(f"Reprovado: {media_final}")

calculo_media()