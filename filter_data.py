import json
from nltk import word_tokenize
import random
from tts_ import execute
from wiki import wiki_
from times import time_
from test1 import moto_
#from what import play_yt



def filter_results(command): # defining a function
    # creating empty lists
    patterns_with_tag = []
    patterns = []
    responses = []
    response_tag = []
    response_with_tag = []
    tokenized_pattern = []

    objects =json.loads(open("data.json").read())  # loading json file

    for object in objects["objects"]:
        for msg in object["patterns"]:
            patterns.append(msg)
            patterns_with_tag.append((msg, object["tag"]))

        for resp in object["response"]:
            responses.append(resp)
            response_with_tag.append((resp, object["tag"]))

    for token in patterns:
        token = word_tokenize(token)
        tokenized_pattern.append(token)

    print("tokenized_pattern:",tokenized_pattern)

    for pattrn in tokenized_pattern:
        for pat in pattrn:
            if pat in command:
                for tag in patterns_with_tag:
                    if pat in tag[0]:
                        t = tag[1]

                        print(t)

                        for result in response_with_tag:
                            if t in result[1]:
                                response_tag.append(result[0])

    print(response_tag)

    if t == "wiki":
        wiki_(command)
    if t == "moto":
        moto_(command)
    if t == "time":
        time_(command)
        
    else:    
        answer = random.choice(response_tag)
        print("command:", command)
        print(answer)
        execute(answer)
                                
 
