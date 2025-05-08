import os

def pastas_arquivos():
 if not os.path.exists("arquivos"):
    os.mkdir("arquivos")

 if not os.path.exists("arquivos/22"):
    os.mkdir("arquivos/22")

 if not os.path.exists("arquivos/23"):
    os.mkdir("arquivos/23")

lista_arquivos = os.listdir("arquivos")
print(lista_arquivos)

for nome_arquivo in lista_arquivos:
    if "txt" in nome_arquivo:
        if "22" in nome_arquivo:
            os.rename(f"arquivos/{nome_arquivo}", f"arquivos/22/{nome_arquivo}")
        elif "23" in nome_arquivo:
            os.rename(f"arquivos/{nome_arquivo}", f"arquivos/23/{nome_arquivo}")

print("Code runs successfully")