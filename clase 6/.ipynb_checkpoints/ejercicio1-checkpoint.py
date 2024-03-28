from pandasai import SmartDataframe
from pandasai.llm import OpenAI

# from pandasai.helpers.openai_info import get_openai_callback
import os

# OpenAI instance model
llm = OpenAI()

df = SmartDataframe("quotations.csv", config={"llm": llm})

# response
response = df.chat(
    "Usando el campo rent como rentabilidad, el campo customer como nombre del cliente, el campo quantity como cantidad de items cotizados. Devolver un grafico de utilizando la libreria plotly que contenga un grafico de barras de los 10 clientes mas rentables promedio"
)

print(response)

# response
response = df.chat(
    "Usando el campo rent como rentabilidad, el campo customer como nombre del cliente, el campo quantity como cantidad de items cotizados. Mostrar la rentabilidad promedio de cada cliente en un grafico de torta."
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
