import discord
import subprocess

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        message_content = message.content
        print(f'Message from [{message.channel.id}] {message.author}: {message_content}')

        if message.channel.id == 941329461322854492:
            if message_content[0] == "/":
                context = ["/usr/local/bin/mcrcon", "-H", "0.0.0.0", "-p", "Hideoareare", "-w", "5", str(message_content[1:])]
                res = ""
                try:
                    res = subprocess.run(context, capture_output=True, text=True)
                except:
                    res = "Error."
                # print(res.stdout)

                print(res)
                await message.channel.send(res.stdout[:-4])

TOKEN = 'XXX'
client = MyClient()
client.run(TOKEN)