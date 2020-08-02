import json

fp = open("test.json","r")

js = json.load(fp)
print(type(js))

