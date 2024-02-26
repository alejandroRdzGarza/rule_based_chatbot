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
    
    
    
    
    
    
    
    
    
    
    
    
elif language == 2:
    print("Hey, I am AlexGPT, a rule-based system created by Alejandro Rodriguez\nI can help you answer almost any question you have about Alex's professional life, hobbies, proyects, etc.")
    print("\n")
    print("Some examples of questions you can ask me: ")
    print("\n")
    print("Where does alex ")
    print("Etc")
    print("\n\n")


while True:
    user_input = input("Message AlexGPT: ")
    nlp_engine.process_input(user_input, language)
    print("\n")
    