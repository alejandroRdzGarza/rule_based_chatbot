import json
import rules_engine
    
def process_input(input_msg):
    if input_msg != "":
        tokenized_words = input_msg.lower().split(" ")
        rules_engine.choose_response(set(tokenized_words))
    else:
        return 
    
    
    
    