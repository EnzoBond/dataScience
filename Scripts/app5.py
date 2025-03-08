# Questão 1:
def eletronics_store():
    precoTotal = 189.987654
    
    print(round(precoTotal, 1))
    print(round(precoTotal, 2))
    print(round(precoTotal, 3))
    
eletronics_store()

# Questão 2:
def school_Notes():
    note1 = 7.356
    note2 = 8.479
    note3 = 6.825
    
    print(round(note1, 1))
    print(round(note2, 1))
    print(round(note3, 1))
    
school_Notes()

# Questão 3:
def lens_function():
    numeros = [5, 10, 15, 20, 25, 30]
    numerosPlus = [5, 10, 15, 20, 25, 30, 35] # Len com o valor extra
    dados = {'nome': 'Ana', 
             'idade': 22, 
             'curso': 'Engenharia'}
    dadosMinus = {'nome': 'Ana', 
                  'idade': 22} # Len com o valor a menos
    valores = (3.14, 2.71, 1.41)
    
    print(len(numeros)) # Resultado: 5
    print(len(numerosPlus)) # Resultado: 6
    print(len(dados)) # Resultado: 3
    print(len(dadosMinus))
    print(len(valores)) # Resultado : 3
    
    
lens_function()

# Questão 4:
def len_function_part2():
    years = [2010, 2012, 2014, 2016, 2018, 2020]
    car_info = {'car_name': 'Kadet', 
                'brand': 'Chevrolet'}
    randomNumbers = (2.53, 13.37, 24.56, 12.56)
    
    print(len(years)) # Resultado : 6
    print(len(car_info)) # Resultado : 2
    print(len(randomNumbers)) # Resultado : 4
    
len_function_part2()

#Questão 5:
def splitting_string():
    artistName = "Travis_Scott"
    
    print(artistName[0])
    print(artistName[4])
    print(artistName[-1])
    print(artistName[0:4])
    print(artistName[0:7])
    
splitting_string()

# Questão 6:
def phrase_splitting():
  frase = "A Galinha botou o ovo."

  print(frase[2:9])
  print(frase[18:23])
  
phrase_splitting()

# Questão 7:
def replace_word():
   phrase = "programar em python e facil"
   
   print(phrase) # Frase normal
   print(phrase.replace("facil", "dificil")) # Frase com a função .replace

replace_word()

# Questão 8:
def upper_lower_names():
    name = "enzo"
    surname = "GABRIEL"
    
    print(name.upper())
    print(surname.lower())
    
upper_lower_names()
    
# Questão 9:
def split_phrases():
    phrase = "I'm streaming on twitch"
    
    print(phrase.split())
    
split_phrases()

# Questão 10:
def input_string():
    nome = input("Qual e o seu nome? ")
    cidade = input("Qual cidade que voce mora? ")
    
    print(f"O seu nome é {nome}")
    print(f"Voce mora na cidade de {cidade}")

input_string()