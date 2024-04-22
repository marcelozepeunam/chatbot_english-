import openai

def detect_grammatical_error(incoming_msg):
    model = "gpt-3.5-turbo"
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": '''Act as an English grammar expert.
                Evaluate whether there is a grammatical error in the input, if so,
                return "True", if not, return "False".
                Do not consider punctuation marks.
                For example:
                1- Input: Hello my name are Lucas
                Output: True
                2- Input: pineapple
                Output: False'''},

                {"role": "user", "content": incoming_msg}
            ]
        )

        grammatical_error_detected = response.choices[0].message['content'].strip().lower()

        # Is there a grammatical error?
        if grammatical_error_detected == 'true':
            print("There is an error") #?Comentar esta linea
            return True
        else:
            print("There is no error") #?Comentar esta linea
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

#Ejemplo de uso
#while True:
#incoming_msg=input("Message: ")
#detect_grammatical_error(incoming_msg)