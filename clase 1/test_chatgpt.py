import os
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

context = "Eres un asistente que usa lógica"

prompts = [
    "Existen dos tipos de personas. Un tipo dice siempre la verdad. El otro siempre miente. Una persona del segundo grupo dice una cosa. Dice una mentira o verdad? ",
    "Una persona corre mas rapido que otra, a su vez esta corre mas rapido que una tercera persona. Quien es el que corre mas rapido y quien mas lento? ",
    "Sabemos que 5 gatos cazan 5 ratones en 5 minutos. Cuanto tiempo toma para que 100 gatos cacen 100 ratones? ",
]

for prompt in prompts:
    conversation = [
        {"role": "system", "content": context},
        {"role": "user", "content": prompt},
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=conversation, max_tokens=50
    )

    message = response.choices[0]["message"]
    print("{}: {}".format(message["role"], message["content"]))
