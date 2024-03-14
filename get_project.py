import os
from dotenv import load_dotenv

# cargamos archivo env
load_dotenv()

proy = "Cargando proyecto: "

print(proy, os.getenv("PROJECT_NAME", "Agregue la variable env PROJECT_NAME"))
# get run mode
run_mode = os.getenv("ENV", "No ENV")
print(run_mode)
# get OPENAI api key
api_key = os.getenv("OPENAI_API_KEY", "No key")
print(api_key)
# end file.
