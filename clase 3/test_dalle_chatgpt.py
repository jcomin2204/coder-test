import os
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

context = "Genera un texto no mayor a 20 palabras para introducir a un modelo generativo texto a imagen"

prompt = "Un jugador de futbol sosteniendo el trofeo con sus manos arriba de su cabeza, papelitos cayendo de arriba y con el resto de jugadores rodeandolo"

conversation = [
    {"role": "system", "content": context},
    {"role": "user", "content": prompt},
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", messages=conversation, max_tokens=50
)

message = response.choices[0]["message"]
print("{}: {}".format(message["role"], message["content"]))

chatGPT_response = response.choices[0]["message"].content

response = openai.Image.create(prompt=chatGPT_response, n=1, size="512x512")
print(response["data"][0]["url"])
