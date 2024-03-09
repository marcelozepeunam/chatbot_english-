#correct_word

import os
import openai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def spelling(sentence):
    sentence = sentence.lower().strip()
    modelo = "gpt-3.5-turbo"
    respuesta = openai.ChatCompletion.create(
        model=modelo,
        messages=[
            {"role": "system", "content": '''Act as an English Teacher. Next I will give you a word in English and you have to correct its grammatical errors.
    As an output I need you to show that same word grammatically corrected.'''},
            {"role": "user", "content": sentence}
        ]
    )
    correct_sentence = respuesta.choices[0].message['content']
    return correct_sentence

# Ejemplo de uso
while True:
    sentence = input("Please enter the word you want to correct: ")
    corrected_sentence = spelling(sentence)
    print("Corrected word:", corrected_sentence)

