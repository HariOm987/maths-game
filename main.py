import os
import discord
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('hello'):
    await message.channel.send('Hello!')
    await message.channel.send("Choose any Number in your mind..... Send 'ok' when you are done")
  
  if message.content.startswith('ok'):
    await message.channel.send('Okay, Nice!! Now multipy it by 2....  Send "done"')

  if message.content.startswith('done'):
    await message.channel.send("So now add 10 to your final number... Send 'alright'")

  if message.content.startswith('alright'):
    await message.channel.send("Now divide your final number by 2 and then subtract your initial number.... Send 'fine' after you are completed with that")

  if message.content.startswith('fine'):
    await message.channel.send("Your Final Number is 5 😍🙌")



keep_alive()  
client.run(os.getenv('TOKEN'))