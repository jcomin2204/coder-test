import os
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")


# Recibe un contexto y genera una respuesta del modelo
def ask_chatgpt(context, conversation, prompt, model, tokens):
    conversation.append(
        {"role": "system", "content": context}, {"role": "user", "content": prompt}
    )

    response = openai.ChatCompletion.create(
        model=model, messages=conversation, max_tokens=tokens
    )

    return response.choices[0]["message"]


# Asistente optimizador de palabras para ser ingresadas a modelo TEXTO -> IMAGEN
context = "Eres un experto diseñador grafico"
prompt = " Genera un logo con contenga la palabra CODER."

# Asistente modelo TEXTO -> IMAGEN
response = openai.Image.create(prompt=prompt, n=1, size="512x512")

# Muestro la imagen generada
print(response["data"][0]["url"])
