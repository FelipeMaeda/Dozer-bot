import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == 'rules':
            while 0 == 0:
                await message.channel.send(f'Caro {message.author.name}, Rules!!')

    async def on_member_join(self,member):
        mensagem = f'{member.mention}, Bem vindo'
        await guild.system_channel.send(mensagem)

    def teste(self):
        message.channel.send(f'Caro {message.author.name}')


client = MyClient()
client.run('OTg0OTQyMjY1NTA2MDk1MTQ1.GMYJHD.8SVDIYeXkJ_0zzvDACkg2QohZjQ8ashM3Ch0pg')