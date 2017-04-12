
import requests
import json

create_url = 'http://localhost:8000/gwent/cards/'

card_list = requests.get('https://api.gwentapi.com/v0/cards?limit=300').json()


for card in card_list['results']:
    url = card['href']

    card_detail = requests.get(url).json()
    categories = []
    positions = []
    if 'categories' in card_detail:
      for cat in card_detail['categories']:
        categories.append({'name': cat['name']})
    if 'positions' in card_detail:
      for pos in card_detail['positions']:
        positions.append({'name': pos})

    card_data = {
        'categories': categories,
        'faction': {
            'name': card_detail['faction']['name']
        },
        'flavor': card_detail['flavor'] if 'flavor' in card_detail else '',
        'group': {
            'name': card_detail['group']['name']
        },
        'availability': {
            'name': card_detail['variations'][0]['availability']
        },
        'rarity': {
            'name': card_detail['variations'][0]['rarity']['name']
        },
        'art':'nothing',
        'name': card_detail['name'],
        'info': card_detail['info'],
        'positions': positions,
    }

    print json.dumps(card_data)
    print requests.post(create_url, json=card_data)
