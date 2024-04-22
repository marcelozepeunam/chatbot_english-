#sentence_correction

import os
import openai
#from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def correct_sentence_grammar(incoming_msg):
    incoming_msg = incoming_msg.lower().strip().replace(".", "").replace(",", "").replace("?", "").replace("!", "")
    modelo = "gpt-3.5-turbo"
    respuesta = openai.ChatCompletion.create(
        model=modelo,
        messages=[
            {"role": "system", "content": '''Act as an English Teacher. Next I will give you a sentence in English and you have to correct the grammatical errors in English.
    As an output I need you to show that same sentence grammatically corrected.'''},
            {"role": "user", "content": incoming_msg}
        ]
    )
    corrected_sentence = respuesta.choices[0].message['content']
    print(corrected_sentence)
    return corrected_sentence

#Ejemplo de uso
'''while True:
    incoming_msg = input("Please enter your message: ")
    print(correct_sentence_grammar(incoming_msg))'''