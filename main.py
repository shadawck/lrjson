"""Lrtemplate 

Usage:
    main.py <file>
    main.py -h|--help
    main.py -v|--version

Options:
    <file>        Lightroom lrtemplate file 
    -h --help     Show this screen.
    -v --version  Show version.
"""

from docopt import docopt
import convert_lr_to_json as cvj


if __name__ == '__main__':

    arguments = docopt(__doc__, version='v0.0.1')

    __file = arguments["<file>"]

    cvj.convert(__file,__file.split(".")[0]+".json")
    print("\033[1;32;40m File converted with Success")
