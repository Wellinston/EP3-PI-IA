import discord

class MyClient(discord.Client):
  async def on_ready(self):
    print("logged on as {0}!" .format(self.user))

  async def on_message(self, message):
    print("Message from {0.author}: {0.content}" .format(message))
    if message.content == "!ola":
      await message.channel.send(f"Olá {message.author.name}! Prazer em conhece-lo")
    if message.content == "!imagem":
      await message.channel.send(file=discord.File("Images/sasuke.jpeg"))
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run("token")
