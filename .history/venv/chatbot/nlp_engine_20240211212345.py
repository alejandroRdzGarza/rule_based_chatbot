import json


def get_responses(json_file_name):
    with open('responses.json') as data:
        responses = json.load(data)
        return responses
    
    
def process_input(input_msg):
    tokenized_words = input_msg.lower().split(" ")
    print(tokenized_words)
    
    
    
# main control loop

while True:
    input_msg = input("You: ")