import nlp_engine

while True:
    print("Hola soy chatbot creado por Alex\nSoy un sistema basado en reglas por lo que soy bastante basico\nAun asi puedo ayudarte a contestar casi cualquier pregunta que tengas sobre Alex. ")
    user_input = input("Message AlexGPT: ")
    nlp_engine.process_input(user_input)
    