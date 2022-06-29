import discord
import os

api_key = os.environ.get('API_KEY')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == 'rules':
            await message.channel.send(f'Caro {message.author.name}, Rules!!')

    async def on_member_join(self,member):
        mensagem = f'{member.mention}, Bem vindo'
        await guild.system_channel.send(mensagem)

    def teste(self):
        message.channel.send(f'Caro {message.author.name}')

client = MyClient()

def test_token(api_key):
    return print(client.loginWithToken(api_key))

def run(api_key):
    client.run(api_key)



#client.run(api_key)