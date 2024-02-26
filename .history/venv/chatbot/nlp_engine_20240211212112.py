import json


def get_responses(json_file_name):
with open('responses.json') as data:
    responses = json.load(data)
    print(responses)