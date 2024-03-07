#counter_word.py 


def counter(sentence):
    sentence = sentence.lower().strip().replace(".", "").replace(",", "").replace("?", "").replace("!", "")
    words_count = len(sentence.split())
    return words_count  # Contar las palabras en la oración

# Ejemplo de uso
# while True:
#     print(len(input("Write a word: ").split()))