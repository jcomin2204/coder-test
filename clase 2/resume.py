import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

print(openai.api_key)


context = "Eres un asistente que realiza resumenes de textos, tu nombre es RES-UM. Debes resumir cualquier texto que te den en no mas de 20 palabras."

# prompt = "El desarrollo del Bluetooth comenzó en 1989 por Nils Rydbeck en Suecia con el objetivo era desarrollar unos auriculares inalámbricos. Trabajó en el proyecto con unos compañeros de la empresa de telecomunicaciones en la que trabajaban: Ericsson Mobile.4​ El diseño y desarrollo principal comenzaron en 1994 y en 1997 el equipo tenía una solución viable.5​ A partir de 1997, Örjan Johansson se convirtió en el líder del proyecto e impulsó la tecnología y la estandarización 6​, haciendo posible que en mayo de 1998 se lanzara la web oficial de Bluetooth."
prompt2 = """31/12/23 20:59 - Porteño: Felicidades chicos ojalá la pasen genial
1/1/24 15:23 - Dieguito Aguirre: Feliz año elite!!! 
Les deseo a cada uno buena salud, muchas oportunidades....pero principalmente mucha felicidad!!
1/1/24 15:26 - Rolo: 🙌🏾🙌🏾🙌🏾🙌🏾🙌🏾🙌🏾👏🏾👏🏾👏🏾👏🏾👏🏾👏🏾
2/1/24 09:07 - Tomas Gonzalez: Feliz año Elitttt!! Por más competencias 💪🏼💪🏼
2/1/24 09:47 - Bruja: Feliz año muchachos🙌🏻🥂
2/1/24 12:23 - Javier Comin: <Multimedia omitido>
2/1/24 12:23 - Javier Comin: 28 de enero tria individual en el puerto
2/1/24 12:23 - Javier Comin: Agenden
2/1/24 12:24 - Rolo: 🙌🏾
2/1/24 12:25 - Tomas Gonzalez: 💪🏽💪🏽
2/1/24 12:32 - Bruja: 🙌🏻
5/1/24 07:35 - Javier Comin: buen dia elite!!  no tienen permiso para hacer el 28 el tria asi que dicen que esta complicada la cosa
5/1/24 07:36 - Javier Comin: luego aviso por novedades
5/1/24 09:30 - Bruja: Buenos días amigos .. dale Javi
5/1/24 09:57 - Rolo: Buenos días grupete… ok ok javi
7/1/24 11:49 - Tomas Gonzalez: 📸 Mira este video en Facebook https://fb.watch/pqsQn_jxBG/?mibextid=v7YzmG
7/1/24 11:51 - Rolo: Le erró feo al bizcachazo
8/1/24 11:31 - Javier Comin: Confirmaron la fecha 28/1 tria
8/1/24 11:31 - Rolo: Presente… 💪🏾
8/1/24 11:31 - Tomas Gonzalez: 💪🏼💪🏼
8/1/24 11:32 - Porteño: Genial
22/1/24 15:07 - Javier Comin: buenas elite! paso info del evento"""

conversation = [
    {"role": "system", "content": context},
    {"role": "user", "content": prompt2},
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", messages=conversation, max_tokens=50
)

message = response.choices[0]["message"]
print("{}: {}".format(message["role"], message["content"]))
