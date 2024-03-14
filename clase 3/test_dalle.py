import os
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

context = "sos pintor de caricaturas a colores"
prompt = "crear un monito con ojos grandes y cara angelical con sus 4 patas que este sentado y tenga puesto auriculares escuchando musica y que en el aire esten los  simbolos de notas musicales."
response = openai.Image.create(prompt=prompt, n=1, size="512x512")
print(response["data"][0]["url"])
