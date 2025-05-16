import sqlite3 as sql

conexao = sql.connect("database.db")

cursor = conexao.cursor()
cursor.execute(
    """
    create table filmes(
        id integer not null primary key autoincrement,
        nome text not null,
        ano int not null,
        nota real not null
        );
        
    """
)

conexao.close()
print("Tabela criada com sucesso!")