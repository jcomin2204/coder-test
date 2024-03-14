import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

print(openai.api_key)


context = "Eres un asistente que realiza generacion de contenidos para redes sociales. Dados ciertos tags debes generar una publicacion armando una historia breve. La historia no debe tener mas de 100 palabras."

prompt = "expertime cronometraje eventos deportivos reconquista corrida 10k"

conversation = [
    {"role": "system", "content": context},
    {"role": "user", "content": prompt},
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", messages=conversation, max_tokens=1000
)

message = response.choices[0]["message"]
print("{}: {}".format(message["role"], message["content"]))
