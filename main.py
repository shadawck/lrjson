import json

fp = open("test.json","r")

js = json.load(fp)

#print(type(js))
#jss = js["value"]["settings"]
#
#for k in js["value"]["settings"]:
#    print(k,":",jss[k])

