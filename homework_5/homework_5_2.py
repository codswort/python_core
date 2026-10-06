import json
from json import JSONDecodeError

data = []
try:
    with open('creds.json', 'r', encoding='utf-8') as f:
        file = json.load(f)
        for x in file:
            data.append({'login' : x['login'],
                         'password' : x['password'],
                         'result' : x['result']})
    for x in data:
        print(f'{x["login"]} - {x["password"]} - {x["result"]}')
except FileNotFoundError as fne:
    print(fne)
except JSONDecodeError as jde:
    print(jde)
except KeyError as ke:
    print(ke)
