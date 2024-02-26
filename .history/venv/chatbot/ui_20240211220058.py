import nlp_engine
print("\n\n\n\n")
print("Hola soy AlexGPT, un sistema basado en reglas creado por alex\n\nPuedo ayudarte a contestar casi cualquier pregunta que tengas sobre Alex. ")
print("Algunos ejemplos de preguntas que puedo contestar: ")
print("Donde estudia ")
print("\n\n")
while True:
    user_input = input("Message AlexGPT: ")
    nlp_engine.process_input(user_input)
    