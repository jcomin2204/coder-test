import os
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

# Generador de contenido para finalizar la historia elegida
context = "Eres un asistente útil"

examples = [
    {
        "pregunta": "El Club Atletico Boca Juniors fue fundado antes o despues que el Club Atletico River Plate?",
        "respuesta": """
Se necesitan repuestas intermedias: Si.
Siguiente: Cuando fue fundado el Club Atletico Boca Juniors?
Respuesta intermedia: El Club Atletico Boca Juniors fue fundado el 3 de Abril de 1905
Siguiente: Cuando fue fundado el Club Atletico River Plate?
Respuesta intermedia: El Club Atletico River Plate fue fundado el 25 de Mayo de 1901
Por lo tanto la respuesta final es: River Plate
""",
    },
    {
        "pregunta": "El Club Atletico Boca Juniors tiene mas copas internacionales que el Club Atletico River Plate?",
        "respuesta": """
Se necesitan repuestas intermedias: Si.
Siguiente: Cuantas copas internacionales tiene el Club Atletico Boca Juniors?
Respuesta intermedia: El Club Atletico Boca Juniors tiene 18
Siguiente: Cuantas copas internacionales tiene el Club Atletico River Plate?
Respuesta intermedia: El Club Atletico River Plate tiene 12
Por lo tanto la respuesta final es: Boca Juniors
""",
    },
    {
        "pregunta": "Argentina tiene mas campeonatos mundiales que Inglaterra?",
        "respuesta": """

Se necesitan repuestas intermedias: Si.
Siguiente: Cuantas veces salio campeon del mundo Argentina en futbol?
Respuesta intermedia: Argentina gano el torneo el 3 ocasiones
Siguiente: Cuantas veces salio campeon del mundo Inglaterra  en futbol?
Respuesta intermedia: Inglaterra gano el torneo el 1 ocasion
Por lo tanto la respuesta final es: Argentina
""",
    },
]

query = "Argentina gano mas copas mundiales que Brasil?"

prompt = f"{examples}\n\nP: {query}\nR"

conversation = [
    {"role": "system", "content": context},
    {"role": "user", "content": prompt},
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", messages=conversation, max_tokens=1000
)

# Muestro la respuesta generada
short_story = response.choices[0]["message"]
print("{}: {}".format(query, short_story["content"]))
