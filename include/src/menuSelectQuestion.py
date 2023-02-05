import discord
from function.userBD import *
from function.questionBD import *
from function.reponseBD import *

class RecupQuestion:
    def __init__(self,user):
        self.question=recupQuestion(user['compteur_question']+1)['contenu']
        self.reponse1=recupReponse(recupQuestion(user['compteur_question']+1)['id_rep_1'])['contenu']
        self.reponse2=recupReponse(recupQuestion(user['compteur_question']+1)['id_rep_2'])['contenu']
        self.idReponse1=recupQuestion(user['compteur_question']+1)['id_rep_1']
        self.idReponse2=recupQuestion(user['compteur_question']+1)['id_rep_2']

#decorateur
class SelectionReponse(discord.ui.Select):
    def __init__(self, question):
        placeholder=f"{question.question}"
        options = [
            discord.SelectOption(
                label=f"{question.reponse1}",emoji="1️⃣", value=f"{question.idReponse1}"
            ),
            discord.SelectOption(
                label=f"{question.reponse2}",emoji="2️⃣", value=f"{question.idReponse2}"
            )
        ]
        super().__init__(
            placeholder=placeholder,
            min_values=1,
            max_values=1,
            options=options,
            )
    async def callback(self,interaction):
        id_question=int(recupUser(interaction.user.id)['compteur_question'])+1
        user=recupUser(interaction.user.id)
        updateCompteurRep(recupReponse(self.values[0])['compteur'],self.values[0])
        updateCompteur(id_question,interaction.user.id)
        updateCompteurRepGenre(self.values[0],user['genre'])
        updateCompteurRegion(self.values[0],user['region'])
        updateCompteurAge(self.values[0],user['age'])
        updateVerif(int(user['verif'])-1,user['id'])
        view=discord.ui.View()
        await interaction.response.edit_message(
            content="Votre réponse a été pris en compte.",view=view
        )