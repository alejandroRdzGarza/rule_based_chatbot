import json
import random

res_eng = [
    {
        "response_type": "greeting",
        "user_input": ["hello", "hi", "hey"],
        "bot_response": "Hey there! I'm your friendly neighborhood chatbot. How can I assist you today?",
        "required_words": []
    },
    {
        "response_type": "welcome_message",
        "user_input": ["what", "do", "you", "do"],
        "bot_response": "Welcome! I'm here to provide information and assistance. You can ask me about Alejandro Rodriguez's education, projects, technical skills, or anything else you'd like to know. Feel free to get creative with your questions!",
        "required_words": ["what", "do", "you", "do"]
    },
    {
        "response_type": "info",
        "user_input": ["who", "is", "alejandro"],
        "bot_response": "Alejandro Rodriguez? He's a software engineering student at Tecnológico de Monterrey.",
        "required_words": ["alejandro", "who"]
    },
    {
        "response_type": "info",
        "user_input": ["where", "does", "alejandro", "study"],
        "bot_response": "Alejandro Rodriguez is a software engineering student at Tecnológico de Monterrey, he will graduate in 2025.",
        "required_words": ["alejandro", "where", "study"]
    },
    {
        "response_type": "info",
        "user_input": ["what", "projects", "has", "alejandro", "worked", "on"],
        "bot_response": "Alejandro Rodriguez has tinkered with various projects, from building apps to creating cool web stuff.",
        "required_words": ["alejandro", "projects"]
    },
    {
        "response_type": "info",
        "user_input": ["what", "are", "alejandro's", "tech", "skills"],
        "bot_response": "Alejandro Rodriguez is a tech wizard! He knows his way around Python, JavaScript, React, TensorFlow, and a bunch of other cool tools.",
        "required_words": ["alejandro", "tech", "skills"]
    },
    {
        "response_type": "info",
        "user_input": ["tell", "me", "something", "interesting", "about", "alejandro"],
        "bot_response": "Did you know Alejandro Rodriguez once debugged a program by whispering sweet nothings to the code? True story!",
        "required_words": ["alejandro", "interesting"]
    },
    {
        "response_type": "info",
        "user_input": ["can", "alejandro", "predict", "the", "future"],
        "bot_response": "Sure, Alejandro Rodriguez can predict the future... of software development! He's always ahead of the game.",
        "required_words": ["alejandro", "predict", "future"]
    },
    {
        "response_type": "info",
        "user_input": ["why", "is", "alejandro", "so", "awesome"],
        "bot_response": "Ah, Alejandro Rodriguez's awesomeness is an unsolved mystery of the universe. Some say it's coded into his DNA.",
        "required_words": ["alejandro", "awesome"]
    },
    {
        "response_type": "info",
        "user_input": ["what", "are", "the", "secrets", "of", "alejandro's", "success"],
        "bot_response": "The secrets of Alejandro Rodriguez's success? 1) Coffee. 2) More coffee. 3) A sprinkle of coding magic.",
        "required_words": ["alejandro", "secrets", "success"]
    },
    {
        "response_type": "prompt",
        "user_input": ["what", "can", "i", "ask"],
        "bot_response": "You can ask me about Alejandro's education, projects, technical skills, or anything else related to his background and experience. Need inspiration? Here are some examples:\n1. Tell me about Alejandro's latest project.\n2. What languages does Alejandro know?\n3. Share an interesting fact about Alejandro.",
        "required_words": ["ask"]
    }
]

res_esp = []



print("Elija un lenguaje")
print("Choose a language")
print("Ingrese 1 para español")
print("Type 2 for english")
language = int(input("hooa"))
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
    print("Where does Alex study at?")
    print("Etc")
    print("\n\n")
    
    
def random_response(language):
    if language == 1:
        print(res_esp[random.randint(0, len(res_esp)-1)]["bot_response"])
        
    elif language == 2:
        print(res_eng[random.randint(0, len(res_eng)-1)]["bot_response"])
        


def choose_response(processed_input, language):
    if language == 1:
        responses = res_esp
    elif language == 2:
        responses = res_eng
    scores_list = []
    for response in responses:
        required_words = set(response["required_words"])
        required_words_score = 0
        general_score = 0
        
        for required_word in required_words:
            if required_word in processed_input:
                required_words_score += 1
                
                
        if required_words_score == len(required_words):
            for word in processed_input:
                if word in response["user_input"]:
                    general_score += 1
                    
        scores_list.append(general_score)
        
        
    best_response = max(scores_list)
    response_index = scores_list.index(best_response)
    
    if best_response != 0:
        print(responses[response_index]["bot_response"])
        
    else:
        
        return random_response(language)
                
            
    
def process_input(input_msg, language):
    if input_msg != "":
        tokenized_words = input_msg.lower().split(" ")
        choose_response(set(tokenized_words), language)
    else:
        print("Please write something so we can talk")
    
    
    

while True:
    if language == 1:
        user_input = input("Preguntame algo: ")
        process_input(user_input, language)
        print("\n")
        
    elif language == 2:
        user_input = input("Message AlexGPT: ")
        process_input(user_input, language)
        print("\n")
    
