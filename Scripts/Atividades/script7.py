# Questão 1:
def questao_1():
    met_pag = str(input("Insira metodo de pagamento (cartao de credito | boleto | pix): "))
    
    if met_pag == "cartao de credito":
        print("Processando o pagamento com o cartão.")
        
    elif met_pag == "boleto":
        print("Processando o pagamento no boleto.")
        
    elif met_pag == "pix":
        print("Processando o pagamento no pix.")
        
    else:
        print("Metodo de pagamento invalido.")
        
questao_1()

# Questão 2:
def questao_2():
    idade = int(input("Qual a sua idade:"))
    
    if idade <= 12:
        print("Você e uma criança.")
        
    elif idade <= 17:
        print("Você e um adolescente.")
        
    elif idade <= 60:
        print("Você e um adulto.")
        
    else:
        print("Você e um idoso.")
        
questao_2()

# Questão 3:
def questao_3():
    valor_total = int(input("Qual e o valor total da compra:"))
    
    if valor_total < 1000:
        print("Você recebeu um desconto de 25%. Agora o valor é: " + valor_total * 0.25)
    
    elif valor_total < 550:
        print("Você recebeu um desconto de 10%. Agora o valor é: " + valor_total * 0.10)
        
    elif valor_total < 100:
        print("Você recebeu um desconto de 05%. Agora o valor é: " + valor_total * 0.05)
        
questao_3()

# Questão 4:
def questao_4():
    tipo_entrega = str(input("Qual e o seu metodo de entrega? (padrão ou expresso) "))
    
    if tipo_entrega == "padrão":
        print("A entrega vai ser R$10.")
    
    elif tipo_entrega == "expresso":
        print("A entrega vai ser R$20.")
        
    else:
        print("Metodo de entrega invalido.")
        
questao_4()

# Questão 5:
def questao_5():
    nota = int(input("Insira sua nota aqui: "))
    
    if nota >= 90:
        print("Aprovado com excelência!")
        
    elif nota < 90:
        print("Aprovado!")
        
    elif nota < 70:
        print("Recuperação!")
        
    elif nota < 50:
        print("Reprovado!")
        
questao_5()

# Questão 6:
def questao_6():
    tempo = int(input("Insira o tempo usado no estacionamento aqui: (Insira o tempo assim:) "))
    
    if tempo == 1:
        print("O estacionamento custou R$5.")
        
    elif tempo <= 3:
        print("O estacionamento custou R$10.")
        
    elif tempo <= 6:
        print("O estacionamento custou R$15.")
    elif tempo > 6:
        print("O estacionamento custou R$25.")
        
questao_6()