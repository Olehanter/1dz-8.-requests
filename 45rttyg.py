

import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)
resp = response.json()

def simile_mind(heros):
    club = {}
    for next_h in heros:
        for act_ in resp:
            if act_['name'] == next_h:
                club[next_h] = act_['powerstats']['intelligence']
                max_intel = max(club.items())
    return (max_intel)


print(simile_mind(['Hulk', 'Captain America', 'Thanos']))
