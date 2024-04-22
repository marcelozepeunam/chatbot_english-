#Modulo main 

import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

# Asegúrate de incluir tus propios módulos de procesamiento de texto aquí
from text_processing.grammar_check import detect_grammatical_error
from text_processing.word_count import counter_words
from text_processing.sentence_correction import correct_sentence_grammar
from text_processing.word_correction import correct_word_grammar
# from text_processing.contextual_conversation import preguntar_chatgpt

app = Flask(__name__)

# Carga las variables de entorno desde .env para mayor seguridad
from dotenv import load_dotenv
load_dotenv()

#Variables de entorno Twilio
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

def process_text_message(incoming_msg):
    # Procesamiento específico para texto
    if detect_grammatical_error(incoming_msg):
        if counter_words(incoming_msg) >= 2:
            corrected_sentence = correct_sentence_grammar(incoming_msg)
            print(corrected_sentence)
            return corrected_sentence
        else:
            corrected_word = correct_word_grammar(incoming_msg)
            print(corrected_word)
            return corrected_word
    else:
        #!Pendiente
        return "Conversación contextual"
        # return preguntar_chatgpt(text)

# #!Pendiente por implementar
# def process_audio_message(incoming_msg):
#     pass

# #!Pendiente por implementar
# def process_multimedia_message(incoming_msg):
#     pass

@app.route('/')
def home():
    return "Bienvenido al Chatbot de WhatsApp", 200

@app.route('/webhook', methods=['POST'])
def webhook():
    # Extrae el mensaje entrante de la solicitud de Twilio
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    # Procesa el mensaje entrante
    response_text = process_text_message(incoming_msg)
    msg.body(response_text)

    return str(resp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
