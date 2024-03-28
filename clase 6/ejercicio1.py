from pandasai import SmartDataframe
from pandasai.llm import OpenAI

# from pandasai.helpers.openai_info import get_openai_callback
import os

# OpenAI instance model
llm = OpenAI()

df = SmartDataframe("titanic.csv", config={"llm": llm})

# response
response = df.chat(
    "Responder en español. Sabiendo que la columna SEX corresponde al genero. Quienes tuvieron mas tasa de supervivencia Hombres o Mujeres? Cuantos del genero sobrevivieron?."
)

print(response)

# # response
# response = df.chat(
#     "Usando el campo categorydetailsname como categoria. Cuantos inscriptos hay en cada categoria? Ordenalos de Mayor a Menor"
# )

# print(response)


# with get_openai_callback() as cb:
#     response = df.chat(
#         "Usando el campo categorydetailsname como categoria. Cuantos inscriptos hay en cada categoria? Ordenalos de Mayor a Menor"
#     )

#     print(response)
#     print(cb)
