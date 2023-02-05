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

def updateCompteurRep(compteur,id):
  compt=accrementation(compteur)
  sql="UPDATE reponse SET compteur=%s WHERE id=%s"
  val=(compt,id)
  cursor.execute(sql,val)
  bd.commit()
    
def updateCompteurRepGenre(id,genre):
  result=recupReponse(id)
  if(genre=="Homme"):
    compt=accrementation(result["compteur_homme"])
    sql="UPDATE reponse SET compteur_homme=%s WHERE id=%s"
    val=(compt,id)
    cursor.execute(sql,val)
  elif(genre=="Femme"):
    compt=accrementation(result["compteur_femme"])
    sql="UPDATE reponse SET compteur_femme=%s WHERE id=%s"
    val=(compt,id)
    cursor.execute(sql,val)
  else:
    compt=accrementation(result["compteur_autre"])
    sql="UPDATE reponse SET compteur_autre=%s WHERE id=%s"
    val=(compt,id)
    cursor.execute(sql,val)
  bd.commit()
  
def updateCompteurRegion(id,region):
  result=recupReponse(id)
  match region:
    case 'ILE-DE-FRANCE':
      compt=accrementation(result["compteur_ile_de_france"])
      sql="UPDATE reponse SET compteur_ile_de_france=%s WHERE id=%s"
      val=(compt,id)
      cursor.execute(sql,val)
    case 'GRAND-EST':
      compt=accrementation(result["compteur_grand_est"])
      sql="UPDATE reponse SET compteur_grand_est=%s WHERE id=%s"
      val=(compt,id)
      cursor.execute(sql,val)
    case 'HAUTS-DE-FRANCE':
      compt=accrementation(result["compteur_hauts_de_france"])
      sql="UPDATE reponse SET compteur_hauts_de_france=%s WHERE id=%s"
      val=(compt,id)
      cursor.execute(sql,val)
    case 'NORMANDIE':
      compt=accrementation(result["compteur_normandie"])
      sql="UPDATE reponse SET compteur_normandie=%s WHERE id=%s"
      val=(compt,id)
      cursor.execute(sql,val)
    case 'BRETAGNE':
      compt=accrementation(result["compteur_bretagne"])
      sql="UPDATE reponse SET compteur_bretagne=%s WHERE id=%s"
      val=(compt,id)
      cursor.execute(sql,val)
    case 'PAYS-DE-LA-LOIRE':
      compt=accrementation(result["compteur_pays_de_la_loire"])
      sql="UPDATE reponse SET compteur_pays_de_la_loire=%s WHERE id=%s"
      val=(compt,id)
      cursor.execute(sql,val)
    case 'CENTRE-VAL-DE-LOIRE':
      compt=accrementation(result["compteur_centre_val_de_loire"])
      sql="UPDATE reponse SET compteur_centre_val_de_loire=%s WHERE id=%s"
      val=(compt,id)
      cursor.execute(sql,val)
    case 'BOURGOGNE-FRANCHE-COMTE':
      compt=accrementation(result["compteur_bourgogne_franche_comte"])
      sql="UPDATE reponse SET compteur_bourgogne_franche_comte=%s WHERE id=%s"
      val=(compt,id)
      cursor.execute(sql,val)
    case 'NOUVELLE-AQUITAINE':
      compt=accrementation(result["compteur_nouvelle_aquitaine"])
      sql="UPDATE reponse SET compteur_nouvelle_aquitaine=%s WHERE id=%s"
      val=(compt,id)
      cursor.execute(sql,val)
    case 'AUVERGNE-RHÔNE-ALPES':
      compt=accrementation(result["compteur_auvergne_rhone_alpes"])
      sql="UPDATE reponse SET compteur_auvergne_rhone_alpes=%s WHERE id=%s"
      val=(compt,id)
      cursor.execute(sql,val)
    case 'OCCITANIE':
      compt=accrementation(result["compteur_occitanie"])
      sql="UPDATE reponse SET compteur_occitanie=%s WHERE id=%s"
      val=(compt,id)
      cursor.execute(sql,val)
    case "PROVENCE-ALPE-COTE-D'AZUR":
      compt=accrementation(result["compteur_provence_alpe_cote_azur"])
      sql="UPDATE reponse SET compteur_provence_alpe_cote_azur=%s WHERE id=%s"
      val=(compt,id)
      cursor.execute(sql,val)
    case 'CORSE':
      compt=accrementation(result["compteur_corse"]) 
      sql="UPDATE reponse SET compteur_corse=%s WHERE id=%s"
      val=(compt,id)
      cursor.execute(sql,val)
    case 'AUTRES REGIONS FRANCAISES':
      compt=accrementation(result["compteur_autre_france"]) 
      sql="UPDATE reponse SET compteur_autre_france=%s WHERE id=%s"
      val=(compt,id)
      cursor.execute(sql,val)
    case 'AUTRES REGIONS DU MONDE':
      compt=accrementation(result["compteur_autre_monde"]) 
      sql="UPDATE reponse SET compteur_autre_monde=%s WHERE id=%s"
      val=(compt,id)
      cursor.execute(sql,val)
  bd.commit()
  
def updateCompteurAge(id,age):
  result=recupReponse(id)
  if(age<18):
    compt=accrementation(result["compteur_mineur"])
    sql="UPDATE reponse SET compteur_mineur=%s WHERE id=%s"
    val=(compt,id)
    cursor.execute(sql,val)
  elif(age<26):
    compt=accrementation(result["compteur_18_25"])
    sql="UPDATE reponse SET compteur_18_25=%s WHERE id=%s"
    val=(compt,id)
    cursor.execute(sql,val)
  elif(age<36):
    compt=accrementation(result["compteur_26_35"])
    sql="UPDATE reponse SET compteur_26_35=%s WHERE id=%s"
    val=(compt,id)
    cursor.execute(sql,val)
  elif(age<51):
    compt=accrementation(result["compteur_36_50"])
    sql="UPDATE reponse SET compteur_36_50=%s WHERE id=%s"
    val=(compt,id)
    cursor.execute(sql,val)
  else:
    compt=accrementation(result["compteur_plus_50"])
    sql="UPDATE reponse SET compteur_plus_50=%s WHERE id=%s"
    val=(compt,id)
    cursor.execute(sql,val)
  bd.commit()
    
def recupReponse(id):
  cursor.execute(f"SELECT Id,	contenu	, compteur, compteur_homme, compteur_femme, compteur_autre, compteur_mineur, compteur_18_25,compteur_26_35, compteur_36_50, compteur_plus_50, compteur_ile_de_france, compteur_grand_est, compteur_hauts_de_france, compteur_normandie, compteur_bretagne, compteur_pays_de_la_loire, compteur_centre_val_de_loire, compteur_bourgogne_franche_comte, compteur_nouvelle_aquitaine, compteur_auvergne_rhone_alpes, compteur_occitanie, compteur_provence_alpe_cote_azur, compteur_corse, compteur_autre_france, compteur_autre_monde	FROM reponse WHERE id={id}")
  result=cursor.fetchall()
  result=result[0]
  return result

def recupDonneCompteurGenre(id):
  cursor.execute(f"SELECT compteur_homme, compteur_femme, compteur_autre FROM reponse WHERE id={id}")
  result=cursor.fetchall()
  result=result[0]
  list=[]
  list2=[]
  i=0
  for element in result:
    list.append(element)
  for element in list:
    list2.append(result[element])
  return list2;

def recupDonneCompteurRegion(id):
  cursor.execute(f"SELECT  compteur_ile_de_france, compteur_grand_est, compteur_hauts_de_france, compteur_normandie, compteur_bretagne, compteur_pays_de_la_loire, compteur_centre_val_de_loire, compteur_bourgogne_franche_comte, compteur_nouvelle_aquitaine, compteur_auvergne_rhone_alpes, compteur_occitanie, compteur_provence_alpe_cote_azur, compteur_corse, compteur_autre_france, compteur_autre_monde FROM reponse WHERE id={id}")
  result=cursor.fetchall()
  result=result[0]
  list=[]
  list2=[]
  i=0
  for element in result:
    list.append(element)
  for element in list:
    list2.append(result[element])
  return list2;

def recupDonneCompteurAge(id):
  cursor.execute(f"SELECT compteur_autre, compteur_mineur, compteur_18_25,compteur_26_35, compteur_36_50, compteur_plus_50 FROM reponse WHERE id={id}")
  result=cursor.fetchall()
  result=result[0]
  list=[]
  list2=[]
  i=0
  for element in result:
    list.append(element)
  for element in list:
    list2.append(result[element])
  return list2;

def recupContenuRep(id):
  cursor.execute(f"SELECT contenu FROM reponse WHERE id={id}")
  result=cursor.fetchall()
  result=result[0]
  return result['contenu']