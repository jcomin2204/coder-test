import os
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")


# Recibe un contexto y genera una respuesta del modelo
def ask_chatgpt(conversation, model, tokens):
    response = openai.ChatCompletion.create(
        model=model, messages=conversation, max_tokens=tokens
    )

    return response.choices[0]["message"]


# Asistente generador de contenido para completar la historia elegida
context = "Eres un asistente que realiza generacion de contenidos. Dada una introduccion debes completar la historia en no mas de 30 palabras."
prompt = "El zorro en el desierto "
model = "gpt-3.5-turbo"
tokens = 1000

conversation = [
    {"role": "system", "content": context},
    {"role": "user", "content": prompt},
]

# Muestro la historia generada
short_story = ask_chatgpt(conversation, model, tokens)
print("{}: {}".format(short_story["role"], prompt + short_story["content"]))

# Asistente optimizador de palabras para ser ingresadas a modelo TEXTO -> IMAGEN
context = "Eres un asistente que genera texto no mayor a 20 palabras para introducir a un modelo generativo texto a imagen"
prompt = prompt + short_story.content

conversation.append({"role": "system", "content": context})
conversation.append({"role": "user", "content": prompt})

short_story_resume = ask_chatgpt(conversation, model, tokens)
print("{}: {}".format(short_story_resume["role"], short_story_resume["content"]))

# Nuevo prompt
prompt = short_story_resume.content

# Asistente modelo TEXTO -> IMAGEN
response = openai.Image.create(prompt=prompt, n=1, size="512x512")

# Muestro la imagen generada
print(response["data"][0]["url"])
