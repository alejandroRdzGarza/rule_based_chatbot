import nlp_engine
print("Elija un lenguaje")
print("Choose a language")
print("Ingrese 1 para español")
print("Type 2 for english")
language = input()
print("\n\n\n\n")
if language == 1:
    
print("Hola soy AlexGPT, un sistema basado en reglas creado por alex\nPuedo ayudarte a contestar casi cualquier pregunta que tengas sobre Alex. ")
print("\n")
print("Algunos ejemplos de preguntas que puedo contestar: ")
print("\n")
print("Donde estudia Alex")
print("Etc")
print("\n\n")
print("Elija un lenguaje")
print("Choose a language")
print("Ingrese 1 para español")
print("Type 2 for english")

while True:
    user_input = input("Message AlexGPT: ")
    nlp_engine.process_input(user_input, language)
    print("\n")
    