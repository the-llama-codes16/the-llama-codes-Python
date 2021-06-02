import json
input='''
[
    {"id":"001","x":"2","name":"Chuck"},
    {"id":"009","x":"7","name":"Brent"}
]'''
info=json.loads(input)
print('Number of Users:',len(info))

for item in info:
    print('\nName:',item['name'])
    print('Attribute:',item['x'])
    print('ID:',item['id'])
    
