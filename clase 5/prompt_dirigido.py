import os
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

# Generador de contenido para finalizar la historia elegida
context = "Eres un asistente útil"

query = "Tomando en cuenta la tabla de paises. Cuales son los paises con mejor calidad de vida?"

prompt = f"{examples}\n\nP: {query}\nR"

conversation = [
    {"role": "system", "content": context},
    {"role": "user", "content": prompt},
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", messages=conversation, max_tokens=1000
)

# Muestro la respuesta generada
first_result = response.choices[0]["message"]
print("{}: {}".format("", first_result["content"]))

prompt = "Especificamente deberias filtrar los paises que no comiencen con A"

conversation.append({"role": "assistant", "content": first_result.content})
conversation.append({"role": "user", "content": prompt})

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", messages=conversation, max_tokens=1000
)

# Muestro la respuesta generada
respuesta_iterativa = response.choices[0]["message"]
print("{}: {}".format(query, respuesta_iterativa["content"]))
