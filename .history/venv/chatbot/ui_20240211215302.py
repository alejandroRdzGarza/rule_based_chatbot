import nlp_engine

while True:
    print("Hola soy chatbot creado por Alex\nSoy un chat ")
    user_input = input("You: ")
    nlp_engine.process_input(user_input)
    