
import json
import re

# Required Transform 
# 1 - Replace all "=" by ":"
# 2 - Add quote on all keyword -> Add quote on all keyword preceded by ":"
# 3 - Replace "{}" by "[]" if there is no a couple "key:value" in it.
# 4 (Cleaning) - Remove "," after all closing "}" or "]"


def convert(infile,outfile):
    
    fin = open(infile,"r")
    fout = open(outfile,"w")


    # 1 - Replace all "=" by ":"
    lines = fin.readlines()
    fout.writelines(lines[0].split()[-1]) # replace "s:{" by "{"
    lines.pop(0) # the first line has already been treated so remove it

    for line in lines:

        # 1 - Replace all "=" by ":"
        line = line.replace("=",":")

        # 2 - Add quote on all keywords preceded by ":"
        replace = re.findall(r"([a-zA-Z0-9]*)\s:",line)
        if len(replace) < 1:
            fout.writelines(line) 
            continue
        line = line.strip("\t").split()
        line = "\"" + replace[0] + "\"" +  "".join(line[1::]) + "\n"

        fout.writelines(line) 

    fin.close()
    fout.close()

    # 3 - Replace "{}" by "[]" if there is no a couple "key:value" in it.
    fout = open(outfile,"rt")
    fdata = fout.read()
    fout.close()
    
    mod1 = re.sub(r"({)\n\t+","[",fdata)
    mod2 = re.sub(r"[0-9]+,\n\t+(})","]",mod1)

    # 4 (Cleaning) - Remove "," after all closing "}" or "]"
    mod3 = re.sub(r"\,(?=\s*?[\}\]])","",mod2)

    fout = open(outfile,"w")
    fout.write(mod3)
    fout.close()

