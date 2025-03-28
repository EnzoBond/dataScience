# Questão 1:
def questao_1():
  print("Questão 1: ")
  vendas = [2800, 3200, 1500, 4000, 5000, 1000, 3500]
  bonus = 0.05

  for venda in vendas:
   if venda >= 3000:
    venda = venda * bonus
    print(venda)
   else:
    bonus = 0
    print(venda)

questao_1()

# Questão 2:
def questao_2():
 print ("Questão 2: ")
 vendas_diarias = [2000, 3000, 2500, 4000, 1800, 5000, 2700]
 meta = 2500
 dias = 0

 for venda in vendas_diarias:
   if venda >= meta:
      dias += 1

 print(dias)

questao_2()

# Questão 3:
def questao_3():
 print("Questão 3: \n")
 vendas = [1500, 2500, 1800, 3200, 4000, 1200, 2800]
 meta = 2000
 bonus = 0.08

 for venda in vendas:
  if venda >= 3000:
   venda = venda * bonus
   print(venda)
  else:
   bonus = 0
   print(venda)

questao_3()

def questão_4():
 print("Questão 4: ")
 lista_vendas = [1000, 500, 800, 1500, 2000, 2300]
 meta = 1200
 objetivo = 0

 for venda in lista_vendas:
  if venda >= meta:
   objetivo += 1

 print(objetivo)
questão_4()

def questao_5():
 print("Questão 5: ")
 lista_vendas = [1000, 500, 800, 1500, 2000, 2300]
 meta = 1200
 venda_bonus = 0
 bonus = 0.1
 bonus_extra = 50

 for venda in lista_vendas:
  if venda >= meta:
    venda_bonus = venda * bonus
    print(venda_bonus)
  elif venda >= 2000:
   venda_bonus = venda * bonus
   print(venda_bonus + bonus_extra)
  else:
   bonus = 0
   print(venda)

questao_5()

def questao_6():
 print("Questão 6: ")
 lista_vendas = [1000, 500, 800, 1500, 2000, 2300]
 
 print(max(lista_vendas))
questao_6()

