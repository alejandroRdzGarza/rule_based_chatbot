import json


def get_responses(json_file_name):
    with open('responses.json') as data:
        responses = json.load(data)
        return responses


def choose_response(processed_input):
    responses = get_responses("responses.json")
    for response in responses:
        required_words = response["required_words"]
        if