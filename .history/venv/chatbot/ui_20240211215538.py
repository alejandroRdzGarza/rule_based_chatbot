import nlp_engine

print("Hola soy AlexGPT creado por Alex\nSoy un sistema basado en reglas por lo que soy bastante basico\nAun asi puedo ayudarte a contestar casi cualquier pregunta que tengas sobre Alex. ")

while True:
    user_input = input("Message AlexGPT: ")
    nlp_engine.process_input(user_input)
    