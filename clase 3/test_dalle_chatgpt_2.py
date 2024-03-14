import os
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

# Generador de contenido para finalizar la historia elegida
context = "Eres un asistente que realiza generacion de contenidos. Dada una introduccion debes completar la historia en no mas de 30 palabras."

prompt = "El zorro en el desierto "

conversation = [
    {"role": "system", "content": context},
    {"role": "user", "content": prompt},
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", messages=conversation, max_tokens=1000
)

# Muestro la historia generada
short_story = response.choices[0]["message"]
print("{}: {}".format(short_story["role"], short_story["content"]))

# Optimizador de palabras para ser ingresadas a modelo TEXTO - IMAGEN
context = "Eres un asistente que genera texto no mayor a 20 palabras para introducir a un modelo generativo texto a imagen"
chatGPT_response = prompt + short_story.content

conversation = [
    {"role": "system", "content": context},
    {"role": "user", "content": chatGPT_response},
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", messages=conversation, max_tokens=50
)

short_story_resume = response.choices[0]["message"]
print("{}: {}".format(short_story_resume["role"], short_story_resume["content"]))

chatGPT_response2 = short_story_resume.content

response = openai.Image.create(prompt=chatGPT_response2, n=1, size="512x512")
print(response["data"][0]["url"])
