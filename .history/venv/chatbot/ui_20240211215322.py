import nlp_engine

while True:
    print("Hola soy chatbot creado por Alex\nSoy un sistema basado en reglas por lo que soy bastante basico ")
    user_input = input("You: ")
    nlp_engine.process_input(user_input)
    