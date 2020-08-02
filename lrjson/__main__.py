"""lrjson

Usage:
    lrjson <file> [--print]
    lrjson -h|--help
    lrjson -v|--version

Options:
    <file>        Lightroom lrtemplate file 
    -p --print    
    -h --help     Show this screen.
    -v --version  Show version.
"""

from docopt import docopt
import subprocess
from lrjson import convert_lr_to_json as cvj

if __name__ == '__main__':

    arguments = docopt(__doc__, version='v0.0.1')

    __file   = arguments["<file>"]
    __out    = __file.split(".")[0]+".json"
    __print  = arguments["--print"] 

    cvj.convert(__file,__out)
    not(__print) and print("\033[1;32;40mFile converted with Success")

    if arguments["--print"]:
        subprocess.run(args=["python3","-m","json.tool",__out])
