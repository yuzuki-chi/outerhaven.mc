import discord
import subprocess
import os
from dotenv import load_dotenv

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        channel_id = os.environ['RCON_CHANNEL']
        message_content = message.content
        print(f'Message from [{message.channel.id}] {message.author}: {message_content}')

        if message.channel.id == channel_id:
            if message_content[0] == "/":
                rcon_path = os.environ['RCON_PATH']
                rcon_pw = os.environ['RCON_PASSWORD']
                context = [rcon_path, "-H", "0.0.0.0", "-p", rcon_pw, "-w", "5", str(message_content[1:])]
                res = ""
                try:
                    res = subprocess.run(context, capture_output=True, text=True)
                except:
                    res = "Error."
                # print(res.stdout)

                print(res)
                await message.channel.send(res.stdout[:-4])

# Load env file => os.environ
load_dotenv()
TOKEN = os.environ['RCON_TOKEN']
client = MyClient()
client.run(TOKEN)