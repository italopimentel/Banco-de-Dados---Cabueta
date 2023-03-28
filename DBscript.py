#banco de dados BD - Cabueta
import sqlite3 as sql

con = sql.connect("noticia.db")
cursor = con.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS
              NoticiaV(
              Link TEXT PRIMARY KEY,
              HeadLine TEXT NOT NULL,
              Content TEXT NOT NULL
              ) ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS
              NoticiaF(
              Link TEXT PRIMARY KEY,
              HeadLine TEXT NOT NULL,
              Content TEXT NOT NULL
              ) ''')

cursor.close()
con.close()