#codigo para chatbot      

import os
import openai
#from openai import OpenAI
from dotenv import load_dotenv



load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

preguntas_anteriores = []
respuestas_anteriores = []

def preguntar_chatgpt(prompt):
    modelo = "gpt-3.5-turbo"
    respuesta = openai.ChatCompletion.create(
        model=modelo,
        messages=[
            {"role": "system", "content": '''Conversemos .'''},
            {"role": "user", "content": prompt}
        ]
    )

    return respuesta.choices[0].message['content']

print('Bienvenido a nuestro chatbot básico. Escribe "salir"  cuando quieras salir')
while True:
    conversacion_historica=""
    texto_usuario = input("Tú: ")
    if texto_usuario.lower() == "salir":
        break

    for pregunta, respuesta in zip(preguntas_anteriores, respuestas_anteriores):
        conversacion_historica += f"El usuario pregunta: {pregunta}\n"
        conversacion_historica += f"Chatbot responde: {respuesta}\n"

    else:
        prompt = f"El usuario pregunta: {texto_usuario}\n"
        conversacion_historica += str(prompt)
        respuesta_gpt = preguntar_chatgpt(conversacion_historica)
        print(respuesta_gpt)

        preguntas_anteriores.append(texto_usuario)
        respuestas_anteriores.append(respuesta_gpt)

