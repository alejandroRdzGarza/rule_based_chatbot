import json
import rules_engine
    
def process_input(input_msg, language):
    if input_msg != "":
        tokenized_words = input_msg.lower().split(" ")
        rules_engine.choose_response(set(tokenized_words))
    else:
        print("Please write something so we can talk")
    
    
    
    