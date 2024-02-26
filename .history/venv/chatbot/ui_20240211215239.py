import nlp_engine

while True:
    print("Hola soy chatbot creado por Alex\nMi principal funcion es")
    user_input = input("You: ")
    nlp_engine.process_input(user_input)
    