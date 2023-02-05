import time
import discord

from function.proposerQuestion import *

class ModalProposerQuestion(discord.ui.Modal):
    def __init__(self, *, title: str = "Proposer un question", custom_id: str = time.time()) -> None:
        super().__init__(title=title)
        
        self.add_item(discord.ui.InputText(label="Question"))
        self.add_item(discord.ui.InputText(label="Réponse 1"))
        self.add_item(discord.ui.InputText(label="Réponse 2"))
    
    async def callback(self, interaction: discord.Interaction):
            if(proposerQuestionBD(interaction.user.id,self.children[0].value,self.children[1].value,self.children[2].value)):
                await interaction.response.send_message("Merci de votre contribution.")
            else:
                await interaction.response.send_message("Vous devez compléter le formulaire ou attendre 5 min.")