import json

path = "./DataFile/data.json"

file = open(path, "rb")
JsonContent = json.load(file)

print(JsonContent)