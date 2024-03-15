import os
import openai
import spacy
from dotenv import load_dotenv

# cargamos archivo env
load_dotenv()

# cargamos el openai api key
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Cargar modelo de spaCy
nlp = spacy.load("es_core_news_sm")


# Recibe un contexto y genera una respuesta del modelo
def ask_chatgpt(conversation, model, tokens):
    response = openai.ChatCompletion.create(
        model=model, messages=conversation, max_tokens=tokens
    )

    return response.choices[0]["message"]


# recetas de pizza
recipes = {
    "recipes": [
        {
            "name": "quattro formaggi",
            "minutes": 5,
            "ingredients": [
                {
                    "name": "masa",
                    "price": 4,
                    "type": "harina 00",
                },
                {
                    "name": "queso",
                    "price": 4,
                    "type": "mozzarella fior di latte",
                },
                {
                    "name": "queso",
                    "price": 2,
                    "type": "provolone picante",
                },
                {
                    "name": "queso",
                    "price": 2,
                    "type": "gorgonzola",
                },
                {
                    "name": "queso",
                    "price": 2,
                    "type": "taleggio",
                },
            ],
        },
        {
            "name": "margherita",
            "minutes": 2,
            "ingredients": [
                {
                    "name": "masa",
                    "price": 4,
                    "type": "harina 00",
                },
                {
                    "name": "queso",
                    "price": 4,
                    "type": "mozzarella fior di latte",
                },
                {
                    "name": "pomodoro",
                    "price": 4,
                    "type": "san marzano",
                },
            ],
        },
        {
            "name": "marinara",
            "minutes": 2,
            "ingredients": [
                {
                    "name": "masa",
                    "price": 4,
                    "type": "harina 00",
                },
                {
                    "name": "evo oil",
                    "price": 0.2,
                    "type": "extra virgin",
                },
                {
                    "name": "pomodoro",
                    "price": 4,
                    "type": "san marzano",
                },
            ],
        },
        {
            "name": "pesto de albahaca",
            "minutes": 6,
            "ingredients": [
                {
                    "name": "masa",
                    "price": 4,
                    "type": "harina 00",
                },
                {
                    "name": "pesto de albahaca",
                    "price": 0.1,
                    "type": "",
                },
                {
                    "name": "ajo",
                    "price": 0.2,
                    "type": "",
                },
                {
                    "name": "queso",
                    "price": 2,
                    "type": "parmigiano reggiano",
                },
                {
                    "name": "queso",
                    "price": 2,
                    "type": "mozzarella fior di latte",
                },
                {
                    "name": "queso",
                    "price": 2,
                    "type": "gorgonzola",
                },
                {
                    "name": "almendras",
                    "price": 1,
                    "type": "",
                },
            ],
        },
        {
            "name": "marinara verde de ajo",
            "minutes": 7,
            "ingredients": [
                {
                    "name": "masa",
                    "price": 4,
                    "type": "harina 00",
                },
                {
                    "name": "anchoas",
                    "price": 3.2,
                    "type": "",
                },
                {
                    "name": "pomodoro",
                    "price": 2,
                    "type": "san marzano",
                },
                {
                    "name": "albahaca",
                    "price": 0.2,
                    "type": "",
                },
                {
                    "name": "ajo",
                    "price": 0.3,
                    "type": "green",
                },
                {
                    "name": "pimienta",
                    "price": 0.1,
                    "type": "",
                },
                {
                    "name": "queso",
                    "price": 2,
                    "type": "parmigiano reggiano",
                },
            ],
        },
    ]
}

examples = [
    {
        "question": "Cual es la receta de la pizza que incluye mayor cantidad de quesos adicionales?",
        "answer": """
            Se necesitan preguntas adicionales: Si.
            Pregunta adicional: El queso muzzarella fior di latte cuenta como queso adicional?
            Respuesta intermedia: No.
            Pregunta adicional: La Quattro Formaggi incluye 3 quesos adicionales?
            Respuesta intermedia: Si.
            Pregunta adicional: La pesto de albahaca tiene 2 quesos adicionales?
            Respuesta intermedia: Si.
            La respuesta final es: La Quattro Formaggi
        """,
    },
    {
        "question": "Cual es el precio de la Quattro Formaggi",
        "answer": """
            Se necesitan preguntas adicionales: Si.
            Pregunta adicional: Cuanto suma el precio de cada ingrediente?
            Respuesta intermedia: 14
            La respuesta final es: 14
        """,
    },
    {
        "question": "Cual es la pizza mas dificil de hacer?",
        "answer": """
            Se necesitan preguntas adicionales: Si.
            Pregunta adicional: Cual es la pizza que lleva mas ingredientes?
            Respuesta intermedia: La marinara verde de ajo
            Pregunta adicional: Cual es la pizza que lleva mas tiempo de preparado?
            Respuesta intermedia: La marinara verde de ajo
            La respuesta final es: La marinara verde de ajo
        """,
    },
]


new_ingredients = [
    "pomodoro, mozzarella y rucula",
    "parmeggiano y peperoni",
    "mortadela, oregano fresco y pistacho crudo",
    "pimienta, oliva y cherries",
    "burrata, jamon crudo y oliva",
]

model = "gpt-4"
tokens = 2000

for new_ingredient in new_ingredients:
    context = "Eres un asistente reconocido mundialmente como chef de pizzas estilo napoletano. "

    prompt = """Deberas tomar en cuenta el contenido en corchetes y las recetas para dar una respuesta

        Dados los ingredientes debes generar:
        - un nombre referente para la pizza gourmet no mayor a 4 palabras
        - completar con un precio estimado conociendo el precio de cada ingrediente. Si se desconoce el precio de un ingrediente estimarlo en base a los ejemplos. No fundamentar.
        - completar con un tiempo estimado de preparado. No fundamentar.
        - una breve descripcion incluyendo cada uno de los ingredientes no mayor a 30 palabras
        - un detalle de receta segun las recetas de ejemplos
        -
        [
            La pizza estilo napolitano, de masa tierna y delgada pero bordes altos, es la versión propia de la cocina napolitana de la pizza redonda.
            El término pizza napoletana, por su importancia histórica o regional, se emplea en algunas zonas como sinónimo de pizza tonda (‘pizza redonda’).
            Bajo la denominación pizza napoletana verace artigianale (‘pizza napolitana auténtica artesanal’) está reconocida como producto agroalimentario tradicional italiano.
            La peculiaridad de la pizza napolitana se debe principalmente a su base, que debe prepararse con masa de pan (completamente desprovista de grasa) tierna y elástica, estirada a mano en forma de disco sin tocar los bordes, que durante la cocción formarán la típica ‘bordes’ (cornicioni) de 1 o 2 cm, mientras que en el centro la masa tendrá unos 3 mm de altura. Un paso rápido por un horno muy caliente debe dejarla húmeda y suave, no demasiado cocida.
            De acuerdo con el pliego de condiciones de la definición de las normas internacionales para la obtención de la marca «Pizza Napolitana» la cocción debe realizarse en horno de leña a unos 485 °C durante unos 90 segundos.
            Algunos afirman que el tomate debe ser de San Marzano.
        ]
    """

    prompt = f"{prompt}\n\n Ingredientes: {new_ingredient}\n\n Recetas: {recipes}\n\n Ejemplos: {examples}"

    # Procesamiento de la oración
    tokenized_prompt = nlp(prompt)

    conversation = [
        {"role": "system", "content": context},
        {"role": "user", "content": tokenized_prompt.text},
    ]

    # Muestro la receta generada
    new_recipe = ask_chatgpt(conversation, model, tokens)
    print("{}".format(new_recipe["content"]))

    # Asistente optimizador de palabras para ser ingresadas a modelo TEXTO -> IMAGEN
    context = "Eres un asistente que genera contenido."
    prompt = "Debes devolver un texto resumido de las recetas para ser introducido en un modelo de AI texto a imagen."
    prompt = f"{prompt}\n\n Receta: {new_recipe.content}\nR"

    conversation.append({"role": "system", "content": context})
    conversation.append({"role": "user", "content": prompt})

    new_recipe_mejorada = ask_chatgpt(conversation, model, tokens)

    # Nueva Receta mejorada
    prompt = new_recipe_mejorada.content

    # Procesamiento de la oración
    tokenized_prompt = nlp(prompt)

    # Asistente modelo TEXTO -> IMAGEN
    response = openai.Image.create(prompt=tokenized_prompt.text, n=1, size="512x512")

    # Muestro la imagen generada
    print("{}".format(response["data"][0]["url"]))

prompt = "Usando informacion de las nuevas recetas. Retornar el nombre de la pizza mas dificil de hacer sin comparar con los ejemplos anteriores."

conversation.append({"role": "user", "content": prompt})
response = ask_chatgpt(conversation, model, tokens)
print("{}".format(response["content"]))
