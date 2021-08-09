import parser
import UPL
import os

class C69_VA:
    def __init__(self, config:dict) -> None:
        self.config = config
        self.parser = parser.parser(config["action_phrases"])
        self.userActions = config["action_phrases"]
    
    def run_userInput(self, userInput:str) -> None:
        userInp = self.parser.parse(userInput)
        
        if userInp[0] not in self.userActions:
            print(chr(69))
            raise Exception("There was an issue, unknown command")
        
        match userInp[0]:
            ## action commands
            case "can":
                pass
            
            ## query commands?
            case "what" | "when" | "how" | "where":
                pass
            
            ## unknown command
            case _:
                pass
    
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





