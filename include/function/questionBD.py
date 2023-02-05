import mysql.connector

from sqlite3 import InternalError, ProgrammingError
from config import *
from .accrementation import *

bd = mysql.connector.connect(
  host = HOST,
  user = USER,
  password = PASSWORD,
  database = DB,
  port = PORT
)

cursor = bd.cursor(dictionary=True)

def recupQuestion(id):
    cursor.execute(f"SELECT contenu, id_rep_1, id_rep_2 FROM question WHERE id={id}")
    result=cursor.fetchall()
    result=result[0]
    return result

def nbQuestion():
    cursor.execute("SELECT COUNT(*) FROM question")
    result=cursor.fetchall()
    result=result[0]['COUNT(*)']
    return result