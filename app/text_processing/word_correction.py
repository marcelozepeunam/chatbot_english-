#word_correction 

import os
import openai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def correct_word_grammar(incoming_msg):
    incoming_msg = incoming_msg.lower().strip()
    modelo = "gpt-3.5-turbo"
    respuesta = openai.ChatCompletion.create(
        model=modelo,
        messages=[
            {"role": "system", "content": '''Act as an English Teacher. Next I will give you a word in English and you have to correct its grammatical errors.
    As an output I need you to show that same word grammatically corrected.'''},
            {"role": "user", "content": incoming_msg}
        ]
    )
    corrected_word = respuesta.choices[0].message['content']
    print(corrected_word)
    return corrected_word

#Ejemplo de uso
'''while True:
incoming_msg = input("Please enter the word you want to correct: ")
corrected_word = correct_word_grammar(incoming_msg)
print("Corrected word:", corrected_word)'''