from voiceEngine import c69_voiceEngine
import parser
import UPL
import sys
import os

class C69_VA:
    def __init__(self, config:dict) -> None:
        self.config = config
        self.funcs = {}
        self.boot()
        self.voice = c69_voiceEngine(self.config)
        self.parser = parser.parser(config["action_phrases"])
        self.userActions = config["action_phrases"]
    
    def run_userInput(self, userInput:str) -> None:
        userInp = self.parser.parse(userInput)
        self.userActions = self.config["action_phrases"]

        if userInp[0] not in self.userActions:
            print(chr(69))
            raise Exception("There was an issue, unknown command")
        
        opt = UPL.Core.switch(self.funcs, userInp[0])
        
        try:
            funcOut = opt(userInp)

            if type(funcOut) == tuple:
                pass
            
        except Exception as e:
            print(chr(69))
            print(e)
        
    def boot(self) -> None:
        if self.config['plugins'] == {}:
            return
        
        for plugin in self.config["plugins"].keys():
            dt = self.config["plugins"][plugin]
            
            ## fancy printing
            print(f"Loading {plugin.capitalize()} version {dt['version']}...")
            print(f"[{plugin}] -> Location: {dt['location']}")
            print(f"[{plugin}] -> {dt['description']}")
    
            ## actually import
            sys.path.append(dt['location'])
            py_script = __import__(plugin)
            
            ## run the plugin
            plugin_data = py_script.plugin_Main()
            cmds = list(plugin_data.keys())
            
            ## append the useful stuff
            self.config["action_phrases"] += cmds
            self.funcs.update(plugin_data)
            
            
            
            
    def main(self) -> None:
        ## main loop
        while True:
            userInput = UPL.Core.ainput("> ", str)
            self.run_userInput(userInput)


## !! SCRIPT START !! ##
if __name__ == "__main__":
    config = UPL.Core.file_manager.getData_json(f"{os.getcwd()}\config.json")
    VA = C69_VA(config)
    VA.main()
    
    


"""
import java.util.Scanner;
public static void main(String[] args){
    System.out.println("Py Is dumb");
    Scanner sc = new Scanner(System.in);
    System.out.println("Is py dumb? Y / N");
    String answer = sc.nextLine();
    if(answer.equals("Y")) {
        System.out.println("Thats based");
    }else if(answer.equals("N") {
        System.out.println("Stop the cap");
    }else {
        System.out.println((char)69);
    }
    
}
"""





