import time
import mysql.connector

from sqlite3 import InternalError, ProgrammingError
from config import *

bd = mysql.connector.connect(
  host = HOST,
  user = USER,
  password = PASSWORD,
  database = DB,
  port = PORT
)

cursor = bd.cursor(dictionary=True)

def proposerQuestionBD(id,question,reponse1,reponse2):
        if(question!=" " and reponse1 !=" " and reponse2!=""):
            sql="INSERT INTO proposition VALUES(%s,%s,%s,%s,%s)"
            val=(time.time(),str(question),int(id),str(reponse1),str(reponse2))
            cursor.execute(sql,val)
            bd.commit()
            return True
        else:
            return False