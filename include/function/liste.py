list_region=['ILE-DE-FRANCE','GRAND-EST','HAUTS-DE-FRANCE','NORMANDIE','BRETAGNE','PAYS-DE-LA-LOIRE','CENTRE-VAL-DE-LOIRE','BOURGOGNE-FRANCHE-COMTE','NOUVELLE-AQUITAINE','AUVERGNE-RHÔNE-ALPES','OCCITANIE',"PROVENCE-ALPE-COTE-D'AZUR",'CORSE','AUTRES REGIONS FRANCAISES','AUTRES REGIONS DU MONDE']
list_genre=['Homme','Femme','Autre']
list_age=['mineur','18-25ans','26-35ans','36-50ans','plus de 50 ans']
list_catagorie=['age','genre','region']

def listGenre(ctx):
    list=['Homme','Femme','Autre']
    return list

def listRegion(ctx):
    list2=[]
    auto=ctx.value
    if auto != None:
        for element in list_region:
            if(element.startswith(auto.upper())):
                list2.append(element)
    return list2

def listCategorie(ctx):
    list2=[]
    auto=ctx.value
    if auto != None:
        for element in list_catagorie:
            if(element.startswith(auto.lower())):
                list2.append(element)
    return list2