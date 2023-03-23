import json
with open('dane_json.json', 'r') as f:
    data = json.load(f)

print(data)
print(data['members'][0])
print(data['members'][0]['powers'][0])