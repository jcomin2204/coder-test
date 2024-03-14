import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

print(openai.api_key)


context = "Eres un asistente que realiza resumenes de textos, tu nombre es RES-UM. Debes resumir cualquier texto que te den en no mas de 20 palabras."

prompt = "El desarrollo del Bluetooth comenzó en 1989 por Nils Rydbeck en Suecia con el objetivo era desarrollar unos auriculares inalámbricos. Trabajó en el proyecto con unos compañeros de la empresa de telecomunicaciones en la que trabajaban: Ericsson Mobile.4​ El diseño y desarrollo principal comenzaron en 1994 y en 1997 el equipo tenía una solución viable.5​ A partir de 1997, Örjan Johansson se convirtió en el líder del proyecto e impulsó la tecnología y la estandarización 6​, haciendo posible que en mayo de 1998 se lanzara la web oficial de Bluetooth."

conversation = [
    {"role": "system", "content": context},
    {"role": "user", "content": prompt},
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", messages=conversation, max_tokens=50
)

chatGPT_response = response.choices[0]["message"].content

context = "Eres un asistente que se encarga de traducir textos del español al ingles."

prompt = "Quiero que traduzcas este texto"
conversation = [
    {"role": "system", "content": context},
    {"role": "assistant", "content": chatGPT_response},
    {"role": "user", "content": prompt},
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", messages=conversation, max_tokens=50, temperature=0
)

message = response.choices[0]["message"]
print("{}: {}".format(message["role"], message["content"]))
