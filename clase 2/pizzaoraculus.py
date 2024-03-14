import os
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")


# Recibe un contexto y genera una respuesta del modelo
def ask_chatgpt(conversation, model, tokens):
    response = openai.ChatCompletion.create(
        model=model, messages=conversation, max_tokens=tokens
    )

    return response.choices[0]["message"]


# Asistente generador de contenido para completar la historia elegida
ingredients = [
    "pomodoro, mozzarella y rucula",
    "parmeggiano y peperoni",
    "mortadela, oregano fresco y pistacho crudo",
    "pimienta, oliva y cherries",
    "burrata, jamon crudo y oliva",
    "tomate",
]
model = "gpt-4"
tokens = 1000

for ingredient in ingredients:
    context = "Eres un asistente reconocido mundialmente como chef de pizzas estilo napoletano. "

    prompt = """Deberas tomar en cuenta el contenido en corchetes para responder.
    Dados los ingredientes de pizzas estilo napoletano debes generar:
        - un nombre referente para la pizza gourmet no mayor a 4 palabras
        - una breve descripcion incluyendo cada uno de los ingredientes no mayor a 30 palabras
        [
            La pizza estilo napolitano, de masa tierna y delgada pero bordes altos, es la versión propia de la cocina napolitana de la pizza redonda. 
            El término pizza napoletana, por su importancia histórica o regional, se emplea en algunas zonas como sinónimo de pizza tonda (‘pizza redonda’). 
            Bajo la denominación pizza napoletana verace artigianale (‘pizza napolitana auténtica artesanal’) está reconocida como producto agroalimentario tradicional italiano.
            La peculiaridad de la pizza napolitana se debe principalmente a su base, que debe prepararse con masa de pan (completamente desprovista de grasa) tierna y elástica, estirada a mano en forma de disco sin tocar los bordes, que durante la cocción formarán la típica ‘bordes’ (cornicioni) de 1 o 2 cm, mientras que en el centro la masa tendrá unos 3 mm de altura. Un paso rápido por un horno muy caliente debe dejarla húmeda y suave, no demasiado cocida.
            De acuerdo con el pliego de condiciones de la definición de las normas internacionales para la obtención de la marca «Pizza Napolitana» la cocción debe realizarse en horno de leña a unos 485 °C durante unos 90 segundos.
            En la más estricta tradición de la cocina napolitana se dan solo dos opciones para la salsa:

            Marinara: con tomate, ajo, orégano y aceite de oliva.a​
            Margherita: con tomate, mozzarella ETG en tiras, mozzarella de búfala campana DOP en cubitos o fior di latte, albahaca y aceite extravirgen de oliva.
            Algunos afirman que el tomate debe ser de San Marzano.            
        ]
    """

    prompt = f"{prompt}\n\n Ingredientes: {ingredient}\nR"

    conversation = [
        {"role": "system", "content": context},
        {"role": "user", "content": prompt},
    ]

    # Muestro el menu generado
    menu = ask_chatgpt(conversation, model, tokens)
    print("{}".format(menu["content"]))

    # Asistente optimizador de palabras para ser ingresadas a modelo TEXTO -> IMAGEN
    context = "Eres un asistente que genera contenido."
    prompt = "Debes devolver un texto mejorado del Menú para ser introducido en un modelo de AI texto a imagen."
    prompt = f"{prompt}\n\n Menú: {menu.content}\nR"

    conversation.append({"role": "system", "content": context})
    conversation.append({"role": "user", "content": prompt})

    menu_mejorado = ask_chatgpt(conversation, model, tokens)

    # Menú mejorado
    prompt = menu_mejorado.content

    # Asistente modelo TEXTO -> IMAGEN
    response = openai.Image.create(prompt=prompt, n=1, size="512x512")

    # Muestro la imagen generada
    print("{}".format(response["data"][0]["url"]))
