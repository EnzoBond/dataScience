import sqlite3 as sql

conexao = sql.connect("database.db")
cursor = conexao.cursor()

cursor.execute(
    """
        insert into filmes (nome, ano, nota)
        values ('Forrest Gump', 1994, 9.5)
    """
)

conexao.commit()
conexao.close()
print("Dados inseridos com sucesso!")

def connect_db():
    conexao = sql.connect("database.db")
    return conexao

def insere_dados(nome, ano, nota):
    conexao = connect_db()
    cursor = conexao.cursor()
    cursor.execute(
        """
            insert into filmes (nome, ano, nota)
            values (?,?,?)
        """,
        (nome, ano, nota)
    )

    conexao.commit()
    conexao.close()
    print("Dados inseridos com sucesso!")

def obter_dados():
    conexao = connect_db()
    cursor = conexao.cursor()
    cursor.execute("select * from filmes")
    dados = cursor.fetchall()
    conexao.close()
    return dados

def excluir_dados():
    conexao = connect_db()
    cursor = conexao.cursor()
    cursor.execute("delete from filmes where id = 1")
    dados = cursor.fetchall()
    conexao.close()
    return
