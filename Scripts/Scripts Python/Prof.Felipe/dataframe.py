import pandas as pd

dic_vendas = {"categoria": ["eletrodomesticos", "games", "livros", "casa"],
              "valor": [20000, 50000, 10000, 200000],
              "quantidade": [200, 500, 300, 1500]}

df_vendas = pd.DataFrame(dic_vendas)

df_vendas

df_vendas.sort_values(by="quantidade", ascending=True).plot.bar()

# Atividade 1:
# Questão 1:
def questao_1():
    produtos = {"Nome":["PS5", "Xbox", "PC Gamer", "PS4"],
                "Preço":["3000", "3000", "2500, 1500"],
                "Estoque":["20", "50", "25", "50"]}
    
    produtos_df = pd.DataFrame(produtos)
    produtos_df

    df_vendas.sort_values(by="Preço", ascending=True).plot.bar()