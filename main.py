import discord
from discord.ext import commands

client = commands.Bot(command_prefix="k!", intents = discord.Intents.all())
client.remove_command("help")

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def bonk(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
            
    bonk = Image.open("bonk.png")
        
    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
        
    pfp = pfp.resize((278,228))
         
    bonk.paste(pfp, (614,232))
        
    bonk.save("profile.png")
        
    await ctx.send(file = discord.File("profile.png"))

@bonk.error
async def bonk_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"You are in cooldown",description=f"Try again in {error.retry_after:.2f}s.", color=discord.Color.orange())
        await ctx.send(embed=em)

client.command()
async def fart(ctx):
    await ctx.send("💩")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! In {round(client.latency * 1000)}ms')

@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= "Reason Not Provided"):
  await ctx.send(member.name + " has Been fart banned from Server 💩 , Because: "+reason)
  await member.ban(reason=reason)

@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason= "Reason Not Provided"):
  await member.send("You Have Been fart kicked from Server 💩  , Because: "+reason)
  await member.kick(reason=reason)

@commands.command(invoke_without_command=True)
async def help(self, ctx):
 embed=discord.Embed(title="List of Available Commands :", color=ctx.author.color)
 embed.set_author(name="HELP!!")
 embed.add_field(name="About EPIK", value="Personal fart bot for Jonah", inline=False)
 embed.add_field(name="`k!ban`", value="fart ban someone from the server(required perms: ban members", inline=False)
 embed.add_field(name="`k!kick`", value="fasrt kick someone from the server(required perms: kick members", inline=False)
 embed.add_field(name="`k!ping`", value="Check my ping (I wont say pong I promise....)", inline=False)
 embed.add_field(name="`k!bonk`", value="To bonk your self or someone usage: k!bonk @someone", inline=False)
 embed.set_footer(text="Try doing k!fart :)")
 await ctx.send(embed=embed)

@client.event
async def on_ready():
  activity = discord.Game(name="k!help | 💩", type=3)
  await client.change_presence(status=discord.Status.do_not_disturb, activity=activity)
  print("fard")

client.run("")