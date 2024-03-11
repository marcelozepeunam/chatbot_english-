from pydub import AudioSegment

def obtener_duracion_audio(audio):
    archivo_audio = AudioSegment.from_mp3(audio)
    duracion = len(archivo_audio) / 1000  # Duración en segundos
    return duracion

audio_path = 'C:\\Users\\Jhassel\\Downloads\\ProyectosPython\\chatbot_english\\audio.mp3'
duracion_audio = obtener_duracion_audio(audio_path)

if duracion_audio > 180:  # 180 segundos = 3 minutos
    print("La duración del audio excede los 3 minutos.")
else:
    print(f'Duración del audio: {duracion_audio} segundos')
