# Questão 1
def questao_um():
  int1 = int(input("Digite o primeiro numero: "))
  int2 = int(input("Digite o segundo numero: "))

  print(f"Os numeros são iguais? {int1, int2}", int1 == int2)
  print(f"O primeiro numero é diferente do segundo? {int1, int2}", int1 != int2)
  print(f"O primeiro numero é maior do que o segundo {int1, int2}", int1 > int2)
  print(f"O primeiro numero é maior ou igual do segundo {int1, int2}", int1 >= int2)
  print(f"O primeiro numero é menor do que o segundo {int1, int2}", int1 < int2)
  print(f"O primeiro numero é menor ou igual do segundo {int1, int2}", int1 <= int2)

questao_um()

# Questão 2
def questao_dois():
 age1 = int(input("Digite a idade da primeira pessoa: "))
 age2 = int(input("Digite a idade da segunda pessoa: "))

 print(f"A idade da primeira pessoa é a mesma da segunda: ", age1 == age2)
 print(f"A idade da primeira pessoa é diferente do que da segunda:", age1 != age2)
 print(f"A idade da primeira pessoa é maior do que da segunda: ", age1 > age2)
 print(f"A idade da primeira pessoa é maior ou igual do que da segunda:", age1 >= age2)
 print(f"A idade da primeira pessoa é menor do que da segunda: ", age1 < age2)
 print(f"A idade da primeira pessoa é menor ou igual do que da segunda:", age1 <= age2)

questao_dois()

# Questão 3:
def questao_tres():
    nota1 = float(input("Insira a nota um: (Variavel não utilizada)"))
    nota2 = float(input("Insira a nota dois: (Variavel não utilizada)"))
    
    print("8.5 é igual a 7.0", 8.5 == 7.0)
    print("8.5 é diferente de 7.0", 8.5 != 7.0)
    print("8.5 é maior que 7.0", 8.5 > 7.0)
    print("8.5 é maior ou igual a 7.0", 8.5 >= 7.0)
    print("8.5 é menor que 7.0", 8.5 < 7.0)
    print("8.5 é menor ou igual a 7.0", 8.5 <= 7.0)
    
questao_tres()
    
# Questão 4:
def questao_quatro():
    paises = ['Brasil', 'Argentina', 'Chile', 'Uruguai']
    
    pais_selecionado = input("Selecione os seguintes paises: Brasil', 'Argentina', 'Chile', 'Uruguai' ")

    print(pais_selecionado in paises)
    print(pais_selecionado not in paises)

questao_quatro()
    
# Questão 5:
def questao_cinco():
    frutas = ['Banana', 'Maça', 'Uva', 'Morango']
    fruta_selecionado = input("Digite o nome de uma fruta: ")
    
    print(fruta_selecionado in frutas)
    print(fruta_selecionado not in frutas)
    
questao_cinco()

# Questão 6:
def questao_seis():
    cores = ['Vermelho', 'Azul', 'Verde', 'Amarelo']
    cor_selecionada = input("Selecione alguma cor: ")
    
    print(cor_selecionada in cores)
    print(cor_selecionada not in cores)
    
questao_seis()

def questao_sete():
    num1 = input("Digite um numero: (Variavel não utilizado)")
    num2 = input("Digite o segundo numero: (Variavel não utilizado)")
    
    print("10 é maior que 5 e 5 é maior que 5: ", 10 > 5 and 5 < 5)
    print("10 é maior que 5 ou 5 é maior que 5: ", 10 > 5 or 10 < 5)
    print("Não é verdade que 10 é menor que 5: ", not 10 > 5)
    
questao_sete()
