# Questão 1:
def question_one():
 print("Resultados para questão 1: \n")
 print("Nome: João Silva")
 print("25 Anos")
 print("Profissão: Desenvolvedor")

 question_one()

# Questão 2:
def product_Information():
    name = input("Qual o nome do produto: ")
    brand = input("Qual e a marca do produto:")
    price = float(input("Qual e o preço do produto: "))
    
    print("Resultados para questão 2: \n")
    print(f"O produto e um: {name}")
    print(f"A marca do seu produto é: {brand}")
    print(f"O preço do produto é: R${price}")

    product_Information()

# Questão 3:
def calculation_1():
    num1 = 15
    num2 = 5
    adicao = num1 + num2
    subtracao = num1 - num2
    multiplicao = num1 * num2
    divisao = num1 / num2
    potencia = num1 ** num2
    
    print("Resultados para questão 3: \n", adicao, "\n", subtracao, "\n", multiplicao, "\n", divisao, "\n", potencia)
 
    calculation_1()

# Questão 4:
def calculation_2():    
    num1 = 7
    num2 = 2
    adicao = num1 + num2
    subtracao = num1 - num2
    multiplicao = num1 * num2
    divisao = num1 / num2
    potencia = num1 ** num2
    
    print("Resultados para questão 4: \n", adicao, "\n", subtracao, "\n", multiplicao, "\n", divisao, "\n", potencia)
    
    calculation_2()
    
#Questão 5:
def school_Information():
    # Lista 
    Materias = ['Filosofia', 'Geografia', 'Sociologia']
    
    # Tuplas
    Notas = (5.4, 6.0, 4.2)
    
    # Dicionario
    Informações = {'nome': 'Di', 'idade': 18, 'curso': 'Ciencias_Humanas'}
    
    print("Resultados para questão 5: \n")
    print(Materias, "\n", Notas, "\n", Informações)
    
    school_Information()
    
# Questão 6:
def car_info():
    Acessorios = ["som", "farois", "escapamento"]
    Especificaçoes = (200, 60)
    info = {'Marca': 'Chevrolet', 'Modelo': 'Cadet', 'Ano': 2007}
    
    print("Resultados para questão 6: \n")
    print(Acessorios, "\n", Especificaçoes, "\n", info)
    car_info()