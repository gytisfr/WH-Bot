#WHBot by ~ Gytis5089

import discord
import asyncio
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '^', intents=discord.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=f"^help"))
    print('WHBot now online.')
    print(f'We are running with {round(client.latency * 100)}ms ping.')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        embed = discord.Embed(
            title="Error",
            colour=0xffffff,
            description="Unknown command,\nCheck your spelling or try again.\nIf this does not work, contact a bot developer."
        )
        embed.set_thumbnail(url="https://i.ibb.co/LpNGYnb/Seal.png")
        embed.add_field(name="Made by", value="Gytis#9668")

def is_gytis(ctx):
    return ctx.author.id in [301014178703998987]
    #Me

def access(ctx):
    return ctx.author.id in [301014178703998987, 807663308949291098]
    #Me, Leo

def is_blacklist(ctx):
    return ctx.author.id in []
    #

@client.command()
async def ping(ctx):
    if is_blacklist(ctx):
        return

    await ctx.send(f":ping_pong: My current ping is {round(client.latency * 100)}ms")

@client.command()
@commands.check(access)
async def status(ctx, *, arg):
    if is_blacklist(ctx):
        return

    await client.change_presence(activity=discord.Game(name=arg))
    await ctx.send(f"My status is now:\n{arg}")

@client.command(aliases=['created', 'join', 'joined'])
async def create(ctx, member : discord.Member = None):
    if is_blacklist(ctx):
        return

    embed = discord.Embed(
        title = 'Create',
        colour = 0xFEFEFE,
        description = f'{member.name} created their account on {str(member.created_at)[0:10]}'
    )
    embed.set_thumbnail(url="https://i.ibb.co/LpNGYnb/Seal.png")
    embed.add_field(name="Made by", value="Gytis#9668")
    await ctx.send(embed=embed)

@client.command(aliases=['suggestion', 'suggests', 'suggestions'])
async def suggest(ctx, *, arg):
    if is_blacklist(ctx):
        return

    embed = discord.Embed(
        title=f'Suggestion',
        colour=0xFEFEFE,
        description=f'**This is from:**<@{ctx.author.id}>\n\n**Suggestion:**{arg}'
    )
    embed.set_thumbnail(url="https://i.ibb.co/LpNGYnb/Seal.png")
    embed.add_field(name="Made by", value="Gytis#9668")
    gytis = client.get_user(301014178703998987)
    await gytis.send(embed=embed)
    await ctx.send('Your suggestion has been sent.')

@client.command(aliases=['purge', 'wipe'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
    if is_blacklist(ctx):
        return

    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(
        title = 'Wipe',
        colour = 0xFEFEFE,
        description = f'{ctx.author.mention} has wiped {amount} messages.'
    )
    embed.set_thumbnail(url="https://i.ibb.co/LpNGYnb/Seal.png")
    embed.add_field(name="Made by", value="Gytis#9668")
    message = await ctx.send(embed=embed)
    await asyncio.sleep(1)
    await message.delete()

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, arg):
    if is_blacklist(ctx):
        return

    embed = discord.Embed(
        title = 'Kick',
        colour = 0xFEFEFE,
        description = f'{ctx.author.mention} has kicked <@{member.id}>'
    )
    embed.set_thumbnail(url="https://i.ibb.co/LpNGYnb/Seal.png")
    embed.add_field(name="Made by", value="Gytis#9668")
    await ctx.send(embed=embed)
    embed = discord.Embed(
        title = 'Kick',
        colour = 0xFEFEFE,
        description = f'{ctx.author.mention} has kicked you.'
    )
    embed.set_thumbnail(url="https://i.ibb.co/LpNGYnb/Seal.png")
    embed.add_field(name="Made by", value="Gytis#9668")
    await member.send(embed=embed)
    await member.kick(reason=arg)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, arg):
    if is_blacklist(ctx):
        return

    embed = discord.Embed(
        title = 'Ban',
        colour = 0xFEFEFE,
        description = f'{ctx.author.mention} has banned <@{member.id}> for:\n{arg}'
    )
    embed.set_thumbnail(url="https://i.ibb.co/LpNGYnb/Seal.png")
    embed.add_field(name="Made by", value="Gytis#9668")
    await ctx.send(embed=embed)
    embed = discord.Embed(
        title = 'Ban',
        colour = 0xFEFEFE,
        description = f'{ctx.author.mention} has banned you for:\n{arg}'
    )
    embed.set_thumbnail(url="https://i.ibb.co/LpNGYnb/Seal.png")
    embed.add_field(name="Made by", value="Gytis#9668")
    await member.send(embed=embed)
    await member.ban(reason=arg)

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    if is_blacklist(ctx):
        return

    embed = discord.Embed(
        title = 'Unban',
        colour = 0xFEFEFE,
        description = f'{ctx.author.mention} has unbanned <@{member.id}>'
    )
    embed.set_thumbnail(url="https://i.ibb.co/LpNGYnb/Seal.png")
    embed.add_field(name="Made by", value="Gytis#9668")
    await ctx.send(embed=embed)
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            try:
                embed = discord.Embed(
                    title = 'Unban',
                    colour = 0xFEFEFE,
                    description = f'{ctx.author.mention} has unbanned you from `{ctx.guild.name}`'
                )
                embed.set_thumbnail(url="https://i.ibb.co/LpNGYnb/Seal.png")
                embed.add_field(name="Made by", value="Gytis#9668")
                await user.send(embed=embed)
            except:
                pass

@client.command(aliases=['guilds', 'guild', 'server'])
@commands.check(access)
async def servers(ctx):
    embed = discord.Embed(
        title='Servers',
        colour=0xFEFEFE
    )
    for guild in client.guilds:
       embed.add_field(name=guild.name, value=f'`ID:`{guild.id}\n`Members:`{guild.member_count}\n`Owner:`{guild.owner}', inline=False)
    embed.set_thumbnail(url="https://i.ibb.co/LpNGYnb/Seal.png")
    embed.add_field(name="Made by", value="Gytis#9668")
    await ctx.author.send(embed=embed)
    await ctx.send('Sent.')

@client.command(aliases=['dm', 'pm', 'msg'])
@commands.check(access)
async def message(ctx, member : discord.Member = None, *, arg):
    if is_blacklist(ctx):
        return

    embed = discord.Embed(
        title=f'Message',
        colour=0xFEFEFE,
        description=f'**This is from:**<@{ctx.author.id}>\n\n{arg}'
    )
    embed.set_thumbnail(url="https://i.ibb.co/LpNGYnb/Seal.png")
    embed.add_field(name="Made by", value="Gytis#9668")
    await member.send(embed=embed)
    await ctx.send('Sent.')

@client.command()
@commands.check(access)
async def say(ctx, *, arg):
    await ctx.send(arg)

@client.command()
@commands.check(access)
async def execannounce(ctx, *, arg):
    if is_blacklist(ctx):
        return

    embed =  discord.Embed(
        title='A Message From the White House:',
        colour =  0xFEFEFE,
        description = f"{arg}"
    )
    embed.set_thumbnail(url="https://i.ibb.co/LpNGYnb/Seal.png")
    embed.add_field(name="Made by", value="Gytis#9668")
    WH = client.get_channel(825689811364478996)
    await WH.send(embed=embed)
    ping = await WH.send('@everyone')
    await ping.delete()


@client.command()
@commands.check(access)
async def execkick(ctx, member : discord.Member, *, arg):
    if is_blacklist(ctx):
        return

    for guild in client.guilds:
        try:
            await guild.kick(member, reason=arg)
        except:
            await ctx.send(f'An error occured, we were unable to kick the member from a server.\nEnsure the bot has administrator permissions and is above the member.\n**Server:**{guild.name}')
    embed = discord.Embed (
        title='Executive Branch Kick',
        colour = 0xFEFEFE,
        description = f"You have been EBK'd\n{arg}"
    )
    embed.set_thumbnail(url="https://i.ibb.co/LpNGYnb/Seal.png")
    embed.add_field(name="Made by", value="Gytis#9668")
    await member.send(embed=embed)

@client.command()
@commands.check(access)
async def execblacklist(ctx, member : discord.Member, *, arg):
    if is_blacklist(ctx):
        return

    for guild in client.guilds:
        try:
            await guild.ban(member, reason=arg)
        except:
            await ctx.send(f'An error occured, we were unable to ban the member from a server.\nEnsure the bot has administrator permissions and is above the member.\n**Server:**{guild.name}')
    embed = discord.Embed (
        title='Executive Branch Blacklist',
        colour = 0xFEFEFE,
        description = f"You have been EBB'd\n{arg}"
    )
    embed.set_thumbnail(url="https://i.ibb.co/LpNGYnb/Seal.png")
    embed.add_field(name="Made by", value="Gytis#9668")
    await member.send(embed=embed)
    embed = discord.Embed (
        title='Executive Branch Blacklist',
        colour = 0xFEFEFE,
        description = f"**User:**{member.mention}\n**Note:**{arg}\n**Blacklister:**{ctx.author.mention}"
    )
    embed.set_thumbnail(url="https://i.ibb.co/LpNGYnb/Seal.png")
    embed.add_field(name="Made by", value="Gytis#9668")
    await member.send(embed=embed)

@client.command()
@commands.check(is_gytis)
async def forceleave(ctx):
    await ctx.send('\U0001f44b')
    await ctx.guild.leave()

@client.command()
@commands.check(is_gytis)
async def leaveall(ctx):
    for guild in client.guilds:
	    await guild.leave()

@client.command()
async def help(ctx):
    if is_blacklist(ctx):
        return

    embed = discord.Embed(
        title='Help',
        colour = 0xFEFEFE,
        description = "__**Public:**__\n`^create` - Check when a user created their account.\n`^suggest` - Leave a suggestion for the bot.\n\n__**Moderation:**__\n`^clear` - Clears specified amount of messages (add 1 when using)\n`^kick` - Kicks the specified member.\n`^ban` - Bans the specified member for the specified reason.\n`^unban` - Unbans the specified member.\n`^message` - Messages the specified user with your message.\n\n__**Exclusive Access:**__\n`^execannounce` - Announces specified message in all servers.\n`^execkick` - Kicks the specified user from all eb discords.\n`^execblacklist` - Bans the specified user from all eb discords.\n`^status` - Allows permitted members to change the bots status.\n`^say` - Makes the bot say what you input after the command.\n`^servers` - See the servers the bot is currently in.\n`^forceleave` - If this bot is found in a server it isn't meant to, <@301014178703998987> can force it to leave.\n`^leaveall` - We got a code red, emergency evacuate every server. (Restricted to <@301014178703998987>)"
    )
    embed.set_thumbnail(url="https://i.ibb.co/LpNGYnb/Seal.png")
    embed.add_field(name="Made by", value="Gytis#9668")
    await ctx.send(embed=embed)

client.run('ODI1NjgyNjUxODEzMTE3OTYy.YGBe5A.kb4MRge9CAmq7ut9mpPM0E4p9Gg')