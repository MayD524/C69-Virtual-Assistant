import UPL
import os

def read_file(args):
    filename = args[1]
    

def open_file(args):
    fileName = args[1]
    if os.path.exists(fileName):
        os.system(fileName)
    else:
        print("That file does not exist")
        
def plugin_Main() -> dict:
    funcs = {
        "open" : open_file
    }
    return funcs