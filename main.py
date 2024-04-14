import discord
import google.generativeai as genai

genai.configure(api_key='AIzaSyDeAtj1nqi5G7OYNvwI8SRC3G9YZAuj6_E')

# Set up the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 10000,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro-001",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[])

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
    convo.send_message(message.content)
    await message.channel.send(convo.last.text)
  elif message.content.startswith('/run'):
    convo.send_message("Run this python code : " + message.content[1:] + "don't describe it and no need to print the code agin just print the output even it give an error, in ``")
    await message.channel.send(convo.last.text)
  elif message.content.startswith('/fix'):
    convo.send_message("fix this python code : " + message.content[1:] + "describe it and give the correct code in ``")
    await message.channel.send(convo.last.text)


client.run('MTIyODU0NTEwOTE1MTMyMjI2NA.Go2g5E.SC8O2xUYZqGX8cFAOh04zFGPqSnz1SfJvCkeWE')
