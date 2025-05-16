import sqlite3 as sql
import numpy as np

def excluir_dados():
 conexao = sql.connect("database.db")
 cursor = conexao.cursor()

 id = ()
 cursor.execute(
     """
     delete from filmes
     where id in(?,?)
     """,
     id
 )

 conexao.commit()
 print("Dados excluidos com sucesso!")