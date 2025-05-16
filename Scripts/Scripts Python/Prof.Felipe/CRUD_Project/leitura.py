import sqlite3 as sql

conexao = sql.connect("database.db")
cursor = conexao.cursor()

dados = cursor.execute("select * from filmes")

print(dados.fetchall())
