import mysql.connector
import plotly.graph_objects as go
import os
import discord
from discord.ext import commands

from config import *
from function.userBD import *
from function.proposerQuestion import *
from function.liste import *
from function.questionBD import *
from function.accrementation import *
from function.reponseBD import *
from function.genrerImage import *
import src.ModalProposerQuestion as modPQ
import src.menuSelectQuestion as menu

bd = mysql.connector.connect(
  host = HOST,
  user = USER,
  password = PASSWORD,
  database = DB,
  port = PORT
)

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    
@bot.slash_command(
  description="liste des commandes", 
  name="command"
)
async def command(ctx):
  embed = discord.Embed(
    title="Commandes",
    description="Liste de toutes les commandes du bot",
    color= discord.Colour.green()
  )
  embed.add_field(name="/register", value="Commande pour s'enregistrer, à faire obligatoirement",inline=False)
  embed.add_field(name="/question", value="Affiche une question aux hasards",inline=False)
  embed.add_field(name="/proposerQuestion [Votre question et les 2 réponses possibles]", value="Ouvre un ticket pour proposer une question",inline=False)
  embed.add_field(name="/totalQuestion", value="Donne le nombre total de question existante",inline=False)
  embed.add_field(name="/resultatQuestion [mettre un numéro]", value="Donne les résultats de la question numéro ...",inline=False)
  embed.add_field(name="/aide", value="Voir ce qu'il faut faire en cas de problème.", inline=False)
  embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/6428/6428802.png")
  embed.set_footer(text="RaynhCoding")
  await ctx.respond(embed=embed)

@bot.slash_command(
  description="Commande pour s'enregistrer",
  name="register"
)
async def register(ctx, age: discord.Option(int, 'age', required=True, min_value=7, max_value=100), 
                   genre: discord.Option(str, 'genre', required=True,autocomplete=listGenre), 
                   region: discord.Option(str, 'region', required=True,autocomplete=listRegion)):
  list_genre=listGenre(ctx)
  if(genre in list_genre):
    if(region in list_region):
      if(enregisterAge(ctx.user.id,age)):
        updateGenre(genre, ctx.user.id)
        updateRegion(region, ctx.user.id)
        await ctx.respond("Vous venez d'être enregistré.")
      else :
        await ctx.respond("Vous etes déjà enregistré.")
    else:
      await ctx.respond("Vous devez choisir une region dans la liste.")
  else:
      await ctx.respond("Vous devez choisir un genre dans la liste idem pour les regions.")
      
@bot.slash_command(
  description="Voir ce qu'il faut faire en cas de problème",
  name="aide"
)
async def aide(ctx):
  embed = discord.Embed(
    title="Aide",
    description="Ce qu'il faut faire en cas de problème",
    color= discord.Colour.green()
  )
  embed.add_field(name="Vous ne pouvez plus répondre à des questions car elle vous dit que vous en avez une en cours.", value="Si vous n'avez pas répondu à la question et que vous avez rejeté le message faite la commande /debug-question (ATTENTION : Elle n'est disponible qu'une fois par jour.)",inline=False)
  embed.add_field(name="Autres problèmes ou bugs", value="Je mettrai bientôt en place un site internet, vous pourrez me contacter dessus dans le futur.",inline=False)
  embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/3288/3288004.png")
  embed.set_footer(text="RaynhCoding")
  await ctx.respond(embed=embed)
  
@bot.slash_command(
  description="Voir ce qu'il faut faire en cas de problème",
  name="debug"
)
@commands.cooldown(rate=1, per=43200,type=commands.BucketType.user)
async def debug(ctx):
  user = recupUser(ctx.user.id)
  if(user!="indexError"):
    if(user['verif']==1):
      updateVerif(0,user['id'])
      await ctx.respond("Vous pouvez continuer à répondre à des questions, Il ne faut surtout pas cliquer sur rejeter avant de répondre aux questions.",ephemeral=True)
    else :
      await ctx.respond("Vous n'avez pas besoin de cette commande.",ephemeral=True)
  else:
    await ctx.respond("Attention vous n'etes pas inscrit, cette commande est faite pour débuger un certain cas que discord ne permet pas pour le moment d'automatiser... elle n'est disponible qu'une seule fois par jour.",ephemeral=True)
  
@bot.event
async def on_application_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    await ctx.respond('La commande pourra être utilisé dans %.2fs'%error.retry_after)
  raise error 
  
@bot.slash_command(
  description="Commande pour proposer une question",
  name="proposer-question",
)
@commands.cooldown(rate=1, per=300, type=commands.BucketType.user)
async def proposerQuestion(ctx):
  await ctx.send_modal(modPQ.ModalProposerQuestion())
  
@bot.slash_command(
  description="Voir le nombre de question qui existe",
  name="nombre-de-question-total"
)
async def nombreDeQuestionTotal(ctx):
  await ctx.respond(f"Le nombre de question total est de {nbQuestion()}")
  
@bot.slash_command(
  description="Voir le nombre de question auxquels tu as répondu.",
  name="nombre-de-question-repondu"
)
async def nbQuestionRepondu(ctx):
  if(recupUser(ctx.user.id)!="indexError"):
    await ctx.respond(f"Le nombre de question auxquels vous avez répondu est de {recupUser(ctx.user.id)['compteur_question']}")
  else:
    await ctx.respond(f"Vous devez vous inscrire.",ephemeral=True)
    
@bot.slash_command(
  description="Répondre à une question",
  name="question",
  ephemeral=True,
)
async def question(ctx):
  user=recupUser(ctx.author.id)
  if(user!="indexError"):
    if(user['compteur_question']!=nbQuestion()):
      if(user['verif']==0):
        updateVerif(int(user['verif'])+1,user['id'])
        user_class=menu.RecupQuestion(user)
        view = discord.ui.View()
        view.add_item(menu.SelectionReponse(user_class))
        await ctx.respond(content="Ne surtout pas rejeter la question",view=view,ephemeral=True)
      else:
        await ctx.respond("Vous avez deja une question en cours.",ephemeral=True)
    else:
        await ctx.respond("Vous avez répondu à toute les questions.")
  else:
    await ctx.respond("Vous devez nous enregistrer avec la commande /register",ephemeral=True)
    
@bot.slash_command(
  description="Permet de voir les répondes d'une question",
  name="reponse-question",
)
async def reponseQuestion(ctx, 
  numero: discord.Option(
    int, 'numero', required=True, min_value=1, max_value=nbQuestion()
  ),
  categorie: discord.Option(str, 'categorie', required=True, autocomplete=listCategorie)
):
  if(categorie in list_catagorie):
    donnee_question=recupQuestion(numero)
    contenu_rep1=recupContenuRep(donnee_question['id_rep_1'])
    contenu_rep2=recupContenuRep(donnee_question['id_rep_2'])
    if not os.path.exists("images"):
      os.mkdir("images")
    if(categorie=='age'):
      donnee_rep1_age=recupDonneCompteurAge(donnee_question['id_rep_1'])
      donnee_rep2_age=recupDonneCompteurAge(donnee_question['id_rep_2'])
      figure=genererImage(list_age,donnee_rep1_age,donnee_rep2_age,contenu_rep1,contenu_rep2)
      figure.write_image("images/fig1.png")
      file = discord.File("images/fig1.png", filename="fig.png")
    elif(categorie=='genre'):
      donnee_rep1_genre=recupDonneCompteurGenre(donnee_question['id_rep_1'])
      donnee_rep2_genre=recupDonneCompteurGenre(donnee_question['id_rep_2']) 
      figure=genererImage(list_genre,donnee_rep1_genre,donnee_rep2_genre,contenu_rep1,contenu_rep2)
      figure.write_image("images/fig2.png")
      file = discord.File("images/fig2.png", filename="fig.png")
    else:
      donnee_rep1_region=recupDonneCompteurRegion(donnee_question['id_rep_1'])
      donnee_rep2_region=recupDonneCompteurRegion(donnee_question['id_rep_2'])
      figure=genererImage(list_region,donnee_rep1_region,donnee_rep2_region,contenu_rep1,contenu_rep2)
      figure.write_image("images/fig3.png")
      file = discord.File("images/fig3.png", filename="fig.png")
    embed = discord.Embed(
      title=f"Résultat de la question {numero}",
      color=discord.Colour.green()
    )
    embed.add_field(name=f"Question :",value=f"{donnee_question['contenu']}", inline=False)
    embed.set_image(url="attachment://fig.png")
    embed.set_footer(text="RaynhCoding")
    await ctx.respond(file=file,embed=embed)
  else:
    await ctx.respond("Vous devez choisir une categorie qui existe.")

bot.run(TOKEN)