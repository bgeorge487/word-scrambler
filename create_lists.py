import requests
def initialize_list():
    url = "https://random-words5.p.rapidapi.com/getMultipleRandom"
    querystring = {"count":"10"}
    headers = {
        "x-rapidapi-key": f'API_KEY',
        "x-rapidapi-host": "random-words5.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    word_list = list(response.json())
    return word_list
# favorite word so far: parleyvoos
# surprising word: clarsachs (returned from the API earlier)
# most fun to say out loud: rhomboids
def not_being_lazy_way():
    word_list_two = ['crash', 'cosmos', 'cob', 'hippo', 'bin', 'bear', 'chinkapins', 'largos', 'felicitates', 'orneriness', 'lithia', 'vertigo',
                     'exposedness', 'engulfment', 'amative', 'capitalistic', 'ramifies', 'rottenness', 'prefix', 'cardiogram', 'flench', 'inosculations',
                     'iota', 'jees', 'foreknown', 'banns', 'divinize', 'indene', 'surmiser', 'chalcographic', 'vertus', 'unconsoled', 'consolidates', 'statutable',
                     'flowingly', 'irrepressibly', 'umbellar', 'socialisation', 'phasmid', 'defamatory', 'quirkily', 'aweless', 'terminability', 'milreis', 'battle-axe',
                     'inexpert', 'quadricentennial', 'perquisite', 'twiddler', 'mutating', 'telpherages', 'collaborator', 'intercolumniation', 'habilitated', 'parleyvoos',
                     'halted', 'consideration', 'daggings', 'accusations', 'rebaptizes', 'recension', 'moats', 'unwieldiness', 'erythematic', 'fractionised',
                     'unfrequented', 'graduates', 'rhomboids', 'mesmerizer', 'admonishing', 'shivery', 'opiated', 'fairly', 'speeds', 'vetoes', 'portolanos',
                     'tokamaks', 'mitzvahs', 'cimbaloms', 'udometers', 'involvements', 'unhandseled', 'sawing', 'advertisements', 'ritualistically','clarsachs']
    return  word_list_two

#     for i in range(10):
#         word_list_two.append(word_list_one[i])
#     print(word_list_two)
#
#
# not_being_lazy_way()