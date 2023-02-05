import plotly.graph_objects as go
import os

def maximun(donnee1,donnee2):
    max=donnee1[0]
    for i in range(len(donnee1)):
        if(max<donnee1[i]):
            max=donnee1[i]
    for i in range(len(donnee2)):
        if(max<donnee2[i]):
            max=donnee2[i]
    return int(max)+1;

def genererImage(categorie,donnee1,donnee2,rep1,rep2):
    categorie=categorie
    figure = go.Figure()
    
    figure.add_trace(go.Scatterpolar(
        r=donnee1,
        theta=categorie,
        fill="toself",
        name=f"{rep1}"
    ))
    
    figure.add_trace(go.Scatterpolar(
        r=donnee2,
        theta=categorie,
        fill="toself",
        name=f"{rep2}"
    ))
    compteur_max=maximun(donnee1,donnee2)
    
    figure.update_layout(
        polar=dict(
            radialaxis=dict(
            visible=True,
            range=[0,compteur_max]
        )),
        showlegend=True
    )
      
    return figure