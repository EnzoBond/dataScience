import sqlite3 as sql

conexao = sql.connect("database.db")
cursor = conexao.cursor()

id = 1
cursor.execute(
    """
        update filmes set nome = ?
        where id = ?
    """,
    ("Forrest Gump", id)
)

conexao.commit()
print("Dados atualizados com sucesso!") 