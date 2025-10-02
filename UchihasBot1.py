import discord

intents = discord.Intents.default()
intents.message_content = True  # important if you want to read messages

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

# Put your bot token inside the quotes
client.run("MTQyMzQxNTkyMzExNjc0MDc5MQ.GQFU3a.j-sWToL6N-Bf9RNWx7a-dFc-J1sWywAHWU8hfg")
