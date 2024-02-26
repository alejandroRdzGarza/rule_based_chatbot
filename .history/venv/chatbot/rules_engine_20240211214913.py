import json
import random

def get_responses(json_file_name):
    with open('responses.json') as data:
        responses = json.load(data)
        return responses
    
def random_response():
    responses = get_responses('responses.json')
    print(responses[random.randint()])


def choose_response(processed_input):
    responses = get_responses("responses.json")
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
        print(responses[best_response]["bot_response"])
        
    else:
        
        return random_response()
                