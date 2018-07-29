import json
from pprint import pprint

data = {}
data['people'] = []

data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})

data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})

data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

# check how does it look like before writing..
# pprint(data, width=60); quit()

# dict data dump(over-write) to json file
with open('./_test/people.json', 'w') as f:
    json.dump(data, f)
