import json
import re
from pprint import pprint

# Required Transform 
# 1 - Replace all "=" by ":"
# 2 - Add quote on all keyword -> Add quote on all keyword preceded by ":"
# 3 - Replace "{}" by "[]" if there is no a couple "key:value" in it.
# 4 (Cleaning) - Remove "," after all closing "}"

fin = open("forest_light_test.lrtemplate","r")
fout = open("forest.json","w")


# 1 - Replace all "=" by ":"
lines = fin.readlines()
fout.writelines(lines[0].split()[-1])
lines.pop(0)

for line in lines:

    # 1 - Replace all "=" by ":"
    line = line.replace("=",":") 

    # 2 - Add quote on all keyword -> Add quote on all keyword preceded by ":"
    replace = re.findall(r"([a-zA-Z0-9]*)\s:",line)
    if len(replace) < 1:
        fout.writelines(line) 
        continue
    line = line.strip("\t").split()
    line = "\"" + replace[0] + "\"" +  "".join(line[1::]) + "\n"


    fout.writelines(line) 

fin.close()
fout.close()

fout = open("forest.json","rt").read()
mod1 = re.sub(r"({)\n\t+","[",fout)         
mod2 = re.sub(r"[0-9]+,\n\t+(})","]",mod1)   

fout = open("final.json","w")
fout.write(mod2)
fout.close()

