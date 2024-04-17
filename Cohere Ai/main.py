import discord
import os
import cohere

TOKEN = os.environ.get("TOKEN")
COHERE_API = os.environ.get("COHERE_API")


co = cohere.Client(COHERE_API) # This is your trial API key



# Discord Stuff

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
  
    
  if message.author == client.user:
    return
  

  if message.content.startswith('!'):
    response = co.generate(
    model='command',
    prompt=message.content,
    max_tokens=300,
    temperature=0.9,
    k=0,
    stop_sequences=[],
    return_likelihoods='NONE')
    await message.channel.send(response.generations[0].text)
#   elif message.content.startswith('/run'):
#     convo.send_message("Run this python code : " + message.content[1:] + "don't describe it and no need to print the code agin just print the output even it give an error, in ``")
#     await message.channel.send(convo.last.text)
#   elif message.content.startswith('/fix'):
#     convo.send_message("fix this python code : " + message.content[1:] + "describe it and give the correct code in ``")
#     await message.channel.send(convo.last.text)

client.run(TOKEN)