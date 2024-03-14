import os
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

# Generador de contenido para finalizar la historia elegida
context = "Eres un asistente útil"

prompt = "Quiero que indiques si la frase es verdadera o falsa. La seleccion Argentina de Futbol usa una camiseta de color Rosado"

conversation = [
    {"role": "system", "content": context},
    {"role": "user", "content": prompt},
]

response = openai.ChatCompletion.create(
    model="gpt-4", messages=conversation, max_tokens=1000
)

# Muestro la historia generada
short_story = response.choices[0]["message"]
print("{}: {}".format(short_story["role"], short_story["content"]))
