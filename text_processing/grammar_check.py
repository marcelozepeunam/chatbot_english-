#grammar_check.py

import os
import openai
#from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def grammar_check_sentence(sentence):
    modelo = "gpt-3.5-turbo"
    respuesta_recetas = openai.ChatCompletion.create(
        model=modelo,
        messages=[
            {"role": "system", "content": '''Actua como experto en gramática de inglés.
            Del input debes de valorar si existe un error gramatical, en caso de que si
            debes de retornar un "True", en caso de que no, retornaras una "False".
            No tomes en cuenta los signos de puntuación.
            Por ejemplo:
            1- Input: Hello my name are Lucas
            Output: True
            2- Input: pineapple
            Output: False'''},
            
            {"role": "user", "content": sentence}
        ]
    )

    return respuesta_recetas.choices[0].message['content']

#Ejemplo de uso
while True:
    sentence = input("\nSentence: ")
    print(grammar_check_sentence(sentence))
