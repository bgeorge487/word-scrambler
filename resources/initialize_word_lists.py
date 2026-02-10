import requests
import os
from dotenv import load_dotenv
# API key protection
load_dotenv()
API_KEY = os.getenv('API_KEY')

def initialize_list():
    url = "https://random-words5.p.rapidapi.com/getMultipleRandom"
    querystring = {"count":"10"}
    headers = {
        "x-rapidapi-key": f'{API_KEY}',
        "x-rapidapi-host": "random-words5.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    word_list = list(response.json())
    return word_list
# favorite word so far: parleyvoos
# Providing some static word lists for more control
def static_word_lists():
    word_list_two = ['crash','cosmos','cob','hippo','bin','bear','chinkapins','largos','felicitates','orneriness'] 
    word_list_three = ['lithia','vertigo','exposedness', 'engulfment', 'amative', 'capitalistic', 'ramifies', 'rottenness', 'prefix', 'cardiogram']
    word_list_four = ['flench','inosculations','iota','parleyvoos','foreknown','banns','divinize','indene','surmiser','chalcographic'] 
    return  word_list_two, word_list_three,word_list_four

#     for i in range(10):
#         word_list_two.append(word_list_one[i])
#     print(word_list_two)
#
#
# not_being_lazy_way()