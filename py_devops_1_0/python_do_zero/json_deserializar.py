import json

with open('meus_pedidos.json') as file:
    json_data = json.load(file)
print(type(json_data))
print(json_data)

json_data_dumps = json.dumps(json_data)
print(json_data_dumps)
json_string = '{"estabelecimento": "Pastelaria DevOps", "pedidos": [{"cliente": "Carlos", "valor": 24.0}, {"cliente": "Jose", "valor": 34.0}]}'

# ## erro proposital
print(type(json_string))
print(json_string)
json_data_s = json.loads(json_string)
print(json_data_s)