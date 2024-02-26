import nlp_engine

res_eng = 


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
    print("Where does Alex study at?")
    print("Etc")
    print("\n\n")


while True:
    if language == 1:
        user_input = input("Preguntame algo: ")
        nlp_engine.process_input(user_input, language)
        print("\n")
        
    elif language == 2:
        user_input = input("Message AlexGPT: ")
        nlp_engine.process_input(user_input, language)
        print("\n")
    
    
    
import json
import random

def get_responses(json_file_name):
    with open(json_file_name) as data:
        responses = json.load(data)
        return responses
    
def random_response():
    responses = get_responses('responses.json')
    print(responses[random.randint(0, len(responses)-1)]["bot_response"])


def choose_response(processed_input, language):
    if language == 1:
        responses = get_responses("res_esp.json")
    elif language == 2:
        responses = get_responses("res_eng.json")
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
        
        return random_response()
                
                
import json
import rules_engine
    
def process_input(input_msg, language):
    if input_msg != "":
        tokenized_words = input_msg.lower().split(" ")
        rules_engine.choose_response(set(tokenized_words), language)
    else:
        print("Please write something so we can talk")
    
    
    
    