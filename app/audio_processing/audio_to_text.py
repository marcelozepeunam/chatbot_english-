# audio_to_text.py (Google spéech recognition)

import speech_recognition as sr
from pydub import AudioSegment
import os
import gc
import pygame  # Importa pygame para reproducir audio

def play_audio(file_path):
    # Inicializa pygame y reproduce el archivo de audio
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    
    # Espera hasta que el audio termine de reproducirse
    while pygame.mixer.music.get_busy():
        continue

def ogg_to_text(ogg_file_path):
    # Convierte ogg a wav para ser compatible con Google Speech Recognition
    audio = AudioSegment.from_ogg(ogg_file_path)
    wav_file_path = ogg_file_path.replace(".ogg", ".wav")
    audio.export(wav_file_path, format="wav")

    # Reproduce el audio original .ogg
    print("Reproduciendo el audio original...")
    play_audio(ogg_file_path)

    # Usa Google Speech Recognition para convertir audio a texto
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_file_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language='es-ES')
        print("Transcripción: " + text)

    # Elimina el archivo WAV creado temporalmente
    os.remove(wav_file_path)

    # Elimina el archivo OGG original
    os.remove(ogg_file_path)

    # Llama al recolector de basura para eliminar cualquier referencia pendiente
    gc.collect()

# Ejemplo de uso
if __name__ == "__main__":
    # Ruta al archivo .ogg que quieres transcribir
    ogg_file_path = 'ejemplo_audio.ogg'
    # Llama a la función pasando la ruta del archivo
    ogg_to_text(ogg_file_path)


