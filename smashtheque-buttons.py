import os
import discord
from discord.ui import Button, View
from discord.ui.item import ItemCallbackType
from discord.ext import commands
import aiohttp

messages = ["""**__Rôles Leboncoin Smashthèque__**
Réagissez aux commandes de votre choix pour vous assigner un rôle!

**__Définitions__**
Je fais partie des <@&777960675150528513> **si je suis un joueur intéressé pour faire partie d'une équipe.**
--> Direction <#777958485434302464> ;

Je fais partie des <@&777960510880219188> **si je suis un capitaine d'équipe intéressé pour recruter un ou des joueurs.**
--> Direction <#777958454152658986> ;

Je fais partie des <@&777960785128980530> **si je suis un streamer intéressé pour streamer les événements d'autres joueurs ou équipes.**
--> Vous serez ping dans <#777958649082937354> et vous pouvez vous présenter dans <#792032632216748042> ;

Je fais partie des <@&777960736508215326> **si je suis un graphiste intéressé pour être tagué afin de venir en aide à une communauté dans la réalisation de graphs, de bannières, ou autre.**
--> Vous serez ping dans <#777958677306277948> et vous pouvez vous présenter dans <#790249146488586281> ;

Je fais partie des <@&798296784433578015> **si je suis un admin de tournoi dispo pour filer un coup de main à un autre admin qui a besoin de soutien pour modérer son tournoi**
--> Vous serez ping dans <#798287271030947862>

💙 = **Joueur libre**
💚 = **Equipe libre**
💜 = **Streamer libre**
❤️ = **Graphiste libre**
💛 = **TO libre**""", """**__Rôles Notifications de mise à jour Smashthèque__**
Réagissez aux commandes de votre choix pour vous assigner un rôle!

**__Définitions__**

Je prends le rôle <@&798300803009478657> **pour être informé de toutes les nouveautés liées à l'agencement, à l'organisation, à l'évolution du Discord**
Je prends le rôle <@&798300268491178034> **pour être informé des mises à jour liées à l'ergonomie du site, aux nouvelles fonctionnalités sur le site et sur Discord**
Je prends le rôle <@&798299938459090984> **pour être informé des mises à jour esthétiques du site web**
Je prends le rôle <@&798299789413974036> **pour être informé d'absolument toutes les mises à jour, mêmes mineures, de l'Observatoire d'Harmonie (ajout de nouvelles et d'anciennes éditions, notamment, ou relectures complètes d'une série de tournois, ou encore ajout de graphs aux éditions qui en sont dépourvues, par exemple)**
Je prends le rôle <@&798963826749079582> **pour être informé de nos tweets et nos mises à jour globales**

<:DrMario:739080111554428948> = **Mises à jour Discord**
<:ROB:737480515946545172> = **Mises à jour développeurs**
<:Graphiste:752212651421204560> = **Mises à jour design**
<:soleil:743285915413250059> = **Mises à jour Harmonie**
<:Falco:739080111852355725> = **Mises à jour Twitter**
""", """**__Rôles Smashthèque 2.0__**
Réagissez aux commandes de votre choix pour vous assigner un rôle!

**__Définitions__**

Je prends le rôle <@&798304550460719135> **si je veux être informé de toute information publiée concernant la Charte du fair-play de la Smashthèque**
Je prends le rôle <@&798305000316600350> **si je suis un TO qui a l'intention de faire appliquer la Charte du fair-play dans son tournoi**

<:Lune:743285273353257051> = **Mises à jour et infos Charte du fair-play**
<:etoile:743286485930868827> = **Candidature TO Charte du fair-play**""", """
**__Synchronisation de mon profil__**
Le rôle <@&738953314237939783> / <@&738952955495186528> vous est automatiquement ajouté si vous êtes notés comme TO d'au moins un tournois. Si vous êtes TO d'un tournois, mais n'avez pas le rôle, cliquez sur le bouton ci dessous pour rafraîchir vos rôles.
Vous pouvez aussi utiliser ce bouton afin de synchroniser vos donnés discord sur votre profil smashthèque (comme votre photo de profil)
"""]

BOT_TOKEN = os.environ.get('PRIVATE_BOT_TOKEN')
BEARER_TOKEN = os.environ.get('SMASHTHEQUE_API_TOKEN')

roles = [777960675150528513]
headers = {"Authorization": f"Bearer {BEARER_TOKEN}", "Content-Type": "application/json"}

async def add_role(interaction: ItemCallbackType, role_id, bot):
    role:discord.Role = bot.get_guild(737431333478989907).get_role(role_id)
    member:discord.Member = bot.get_guild(737431333478989907).get_member(interaction.user.id)
    for member_role in member.roles:
        if role == member_role:
            await member.remove_roles(role)
            await interaction.response.send_message(f"Le rôle {role.mention} vous a été retiré", ephemeral=True)
            return

    await member.add_roles(role)
    await interaction.response.send_message(f"Le rôle {role.mention} vous a été ajouté", ephemeral=True)

class PersistantButtonsFirst(View):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(timeout=None)

    @discord.ui.button(label="Joueurs Libres", style= discord.ButtonStyle.blurple, custom_id='role_button:JoueursLibres', emoji="💙")
    async def JoueursLibres(self, button: discord.ui.Button, interaction: discord.Integration):
        role_id = 777960675150528513
        await add_role(interaction, role_id, self.bot)
    @discord.ui.button(label="Equipes Libres", style= discord.ButtonStyle.blurple, custom_id='role_button:EquipesLibres', emoji="💚")
    async def EquipesLibres(self, button: discord.ui.Button, interaction: discord.Integration):
        role_id = 777960510880219188
        await add_role(interaction, role_id, self.bot)
    @discord.ui.button(label="Streamers Libres", style= discord.ButtonStyle.blurple, custom_id='role_button:StreamersLibres', emoji="💜")
    async def StreamersLibres(self, button: discord.ui.Button, interaction: discord.Integration):
        role_id = 777960785128980530
        await add_role(interaction, role_id, self.bot)
    @discord.ui.button(label="Graphistes Libres", style= discord.ButtonStyle.blurple, custom_id='role_button:GraphistesLibres', emoji="❤️")
    async def GraphistesLibres(self, button: discord.ui.Button, interaction: discord.Integration):
        role_id = 777960736508215326
        await add_role(interaction, role_id, self.bot)
    @discord.ui.button(label="TOs Libres", style= discord.ButtonStyle.blurple, custom_id='role_button:TOsLibres', emoji="💛")
    async def TOsLibres(self, button: discord.ui.Button, interaction: discord.Integration):
        role_id = 798296784433578015
        await add_role(interaction, role_id, self.bot)

class PersistantButtonsSecond(View):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(timeout=None)

    @discord.ui.button(label="Mises à jour Discord", style=discord.ButtonStyle.blurple, custom_id="role_button:UpdatesDiscord", emoji=discord.PartialEmoji(id=739080111554428948, name="DrMario"))
    async def UpdatesDiscord(self, button: discord.ui.Button, interaction: discord.Integration):
        role_id = 798300803009478657
        await add_role(interaction, role_id, self.bot)

    @discord.ui.button(label="Mises à jour Devs", style=discord.ButtonStyle.blurple, custom_id="role_button:UpdatesDevs", emoji=discord.PartialEmoji(id=737480515946545172, name="ROB"))
    async def UpdatesDevs(self, button: discord.ui.Button, interaction: discord.Integration):
        role_id = 798300268491178034
        await add_role(interaction, role_id, self.bot)

    @discord.ui.button(label="Mises à jour Design", style=discord.ButtonStyle.blurple, custom_id="role_button:UpdatesDesign", emoji=discord.PartialEmoji(id=752212651421204560, name="Graphiste"))
    async def UpdatesDesign(self, button: discord.ui.Button, interaction: discord.Integration):
        role_id = 798299938459090984
        await add_role(interaction, role_id, self.bot)

    @discord.ui.button(label="Mises à jour Harmonie", style=discord.ButtonStyle.blurple, custom_id="role_button:UpdatesHarmonie", emoji=discord.PartialEmoji(id=743285915413250059, name="soleil"))
    async def UpdatesHarmonie(self, button: discord.ui.Button, interaction: discord.Integration):
        role_id = 798299789413974036
        await add_role(interaction, role_id, self.bot)

    @discord.ui.button(label="Mises à jour Twitter", style=discord.ButtonStyle.blurple, custom_id="role_button:UpdatesTwitter", emoji=discord.PartialEmoji(id=739080111852355725, name="Falco"))
    async def UpdatesTwitter(self, button: discord.ui.Button, interaction: discord.Integration):
        role_id = 798963826749079582
        await add_role(interaction, role_id, self.bot)

class PersistantButtonsThird(View):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(timeout=None)

    @discord.ui.button(label="Mises à jour Fair Play", style=discord.ButtonStyle.blurple, custom_id="role_button:UpdatesFairPlay", emoji=discord.PartialEmoji(id=743285273353257051, name="Lune"))
    async def UpdatesFairPlay(self, button: discord.ui.Button, interaction: discord.Integration):
        role_id = 798304550460719135
        await add_role(interaction, role_id, self.bot)

    @discord.ui.button(label="Candidatures Fair Play", style=discord.ButtonStyle.blurple, custom_id="role_button:CandidaturesFairPlay", emoji=discord.PartialEmoji(id=743286485930868827, name="etoile"))
    async def CandidaturesFairPlay(self, button: discord.ui.Button, interaction: discord.Integration):
        role_id = 798305000316600350
        await add_role(interaction, role_id, self.bot)

class PersistantButtonFourth(View):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(timeout=None)
        self.session = aiohttp.ClientSession(headers=headers)

    @discord.ui.button(label="Rafraîchir mon profil", style=discord.ButtonStyle.green, custom_id="role_button:RefreshProfile", emoji=discord.PartialEmoji(id=867082118063849472, name="emoji_reload"))
    async def RefreshProfile(self, button: discord.ui.Button, interaction: discord.Integration):
        async with self.session.get(f'https://www.smashtheque.fr/api/v1/discord_users/{interaction.user.id}/refetch') as resp:
            if resp.status == 404:
                await interaction.response.send_message(f"Vous n'êtes pas enregistrés dans la smashthèque !\nVous pouvez vous enregistrer sur https://smashtheque.fr/users/me, où en suivant les instructions dans <#750022794007412746>.", ephemeral=True)
            elif resp.status == 200:
                await interaction.response.send_message(f"Votre profil a été mis à jour avec succès !", ephemeral=True)
            else:
                await interaction.response.send_message(f"Il y a eu un problème durant la mise à jour de votre profil.", ephemeral=True)
                await self.bot.get_channel(747201417454026802).send(f"Il y a eu un problème durant la mise à jour d'un profil. Traceback : \nutilisateur : {interaction.user}\nID utilisateur : {interaction.user.id}\nstatus code : {resp.status}\nréponse : {resp}")



class ApplicationsTeam(Button):
    async def callback(self, interaction):
        print(interaction)




class SmashthequeRoles(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('$'), intents=discord.Intents.all())
        self.persistent_views_added = False

    async def on_ready(self):
        if not self.persistent_views_added:
            self.add_view(PersistantButtonsFirst(self))
            self.add_view(PersistantButtonsSecond(self))
            self.add_view(PersistantButtonsThird(self))
            self.add_view(PersistantButtonFourth(self))
            self.persistent_views_added = True


        #await channel.send(messages[3], view=PersistantButtonFourth(self))
    
bot = SmashthequeRoles()

@bot.command(name="setupmessages")
@commands.is_owner()
async def setupmessages(ctx: commands.context):
    channel = bot.get_guild(737431333478989907).get_channel(861337441339047957)
    await channel.send(messages[0], view=PersistantButtonsFirst(bot))
    await channel.send(messages[1], view=PersistantButtonsSecond(bot))
    await channel.send(messages[2], view=PersistantButtonsThird(bot))
    await channel.send(messages[3], view=PersistantButtonFourth(bot))

bot.run(BOT_TOKEN)