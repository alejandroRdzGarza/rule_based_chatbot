import nlp_engine

print("Hola soy AlexGPT un sistema basado en reglas creado por alex\nAun asi puedo ayudarte a contestar casi cualquier pregunta que tengas sobre Alex. ")

while True:
    user_input = input("Message AlexGPT: ")
    nlp_engine.process_input(user_input)
    