#word_count.py (Jhassel)

def counter_words(incoming_msg):
    incoming_msg = incoming_msg.lower().strip().replace(".", "").replace(",", "").replace("?", "").replace("!", "")
    words_count = len(incoming_msg.split())
    return words_count  # Contar las palabras en la oración

# Ejemplo de uso
# while True:
#     print(len(input("Write a word: ").split()))