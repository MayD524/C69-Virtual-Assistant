import subprocess
import UPL
import os

class filemgr:
    def __init__(self, config:dict) -> None:
        self.config = config

    def read_file(self, args:list) -> tuple:
        filename = args[1]
        lines = UPL.Core.file_manager.clean_read(filename)
        
        return ("read_lines", lines)

    def open_file(self, args:list) -> tuple:
        fileName = args[1]
        if os.path.exists(fileName):
            os.system(fileName)
        else:
            return ("say", "That file does not exist")
    
    def run_file(self, args:list) -> tuple:
        program = args[1]
        try:
            subprocess.Popen(program)
        
        except:
            return ("say", "That program does not exist")
        
def plugin_Main(config:dict) -> dict:
    flmgr = filemgr(config)
    funcs = {
        "open" : flmgr.open_file,
        "read" : flmgr.read_file,
        "run"  : flmgr.run_file
    }
    
    return funcs