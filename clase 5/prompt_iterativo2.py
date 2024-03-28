import os
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

# Generador de contenido para finalizar la historia elegida
context = "Eres un asistente útil"

examples = """
País	Cantidad de habitantes	Índice de calidad de vida
Argentina	283471250	7.92
Brasil	202175402	7.59
Chile	79191392	3.55
Colombia	91106897	1.4
Ecuador	15585653	0.66
México	138436201	0.64
Perú	133310908	9.1
Uruguay	156708946	7.61
Venezuela	38511435	4.91
Guatemala	18646161	8.45
Cuba	134002149	8.35
Bolivia	127408905	0.96
Paraguay	89645984	3.34
Costa Rica	246367212	9.15
Nicaragua	173046872	3.8

"""

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
first_response = response.choices[0]["message"]
print("{}: {}".format(first_response["role"], first_response["content"]))


prompt = "Filtrar o excluir de la tabla anterior los paises que comiencen con A"

conversation.append(
    {
        "role": "assistant",
        "content": ("{}: {}".format(first_response["role"], first_response["content"])),
    }
)

conversation.append(
    {
        "role": "user",
        "content": prompt,
    }
)

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", messages=conversation, max_tokens=1000
)

# Muestro la respuesta generada
last_response = response.choices[0]["message"]
print("{}: {}".format(query, last_response["content"]))
