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

def updateVerif(verif,id):
    sql="UPDATE user SET verif=%s WHERE id=%s"
    val=(verif,id)
    cursor.execute(sql,val)
    bd.commit()
    
def updateCompteur(compteur,id):
    sql="UPDATE user SET compteur_question=%s WHERE id=%s"
    compteur=int(compteur)
    val=(compteur,id)
    cursor.execute(sql,val)
    bd.commit()
    
def updateGenre(genre,id):
    sql="UPDATE user SET genre=%s WHERE id=%s"
    val=(genre,id)
    cursor.execute(sql,val)
    bd.commit()
    
def updateRegion(region,id):
    sql="UPDATE user SET region=%s WHERE id=%s"
    val=(region,id)
    cursor.execute(sql,val)
    bd.commit()
    
def updateAge(age,id):
    sql="UPDATE user SET age=%s WHERE id=%s"
    val=(age,id)
    cursor.execute(sql,val)
    bd.commit()
    
#recupération des données de l'utilisateur par un id    
def recupUser(id):
    try:
        cursor.execute(f"SELECT id,genre,age,compteur_question,region,verif FROM user WHERE id={id}")
        result=cursor.fetchall()
        result=result[0]
        return result
    except IndexError:
        return "indexError"
    
def enregisterAge(id,age):
    try:
        id=int(id)
        sql = "INSERT INTO user VALUES (%s,%s,%s,%s,%s,%s)"
        val = (id, "aucun",age,0,"aucun",0)
        cursor.execute(sql, val)
        bd.commit()    
        return True;      
    except mysql.connector.errors.IntegrityError:
        return False;
    
def verifGenre(id,genre):
    try:
        id=int(id)
        genre=str(genre)
        cursor.execute(f"SELECT genre FROM user WHERE id={id}")
        result=cursor.fetchall()
        result=result[0]
        if(result['genre']=="aucun"):
            updateGenre(genre,id)
            return True
        else:
            return False
    except IndexError:
            return False
        
def verifRegion(id,region):
    try:
        id=int(id)
        region=str(region)
        cursor.execute(f"SELECT region FROM user WHERE id={id}")
        result=cursor.fetchall()
        result=result[0]
        if(result['region']=="aucun"):
            updateRegion(region,id)
            return True
        else:
            return False
    except IndexError:
            return False