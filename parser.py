import json

# read file
with open('data/data.json', 'r') as jsonfile:
  data = jsonfile.read()

# parse file
obj = json.loads(data)

# write nation file
with open('data/nation.json', 'w') as nationfile:
  nations = {}
  nations['data'] = []

  for data in obj[0]['data']:
    nations['data'].append({
      'name': data['nation'],
      'recap': [],
    })
  
  idx = 0
  for data in obj:
    for nation in nations['data']:
      nation['recap'].append({
        'date': data['date'],
        'point': 0,
      })
    for country in data['data']:
      for state in nations['data']:
        if country['nation'] == state['name']:
          state['recap'][idx]['point'] = country['point']
    idx += 1

  json.dump(nations, nationfile, indent=2)