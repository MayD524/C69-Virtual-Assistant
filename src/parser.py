import re
## it works on my machine ¯\_(ツ)_/¯
class parser:
    def __init__(self, action_phrases:list) -> None:
        self.action_phrases = action_phrases

    def parse(self, string:str) -> list:

        command_list = []
        string = string.lower()
        string = string.rsplit("?",1)[0]
        string = string.split(" ") #Sweden idea works all the time i guess?
        commandPhrase = string[:len(string) // 2]
        
        """
            Can   - can you <action>
            What  - what was <question>
            When  - when was <question>
            How   - how was | how is <question>
            Where - Where is <question>
            Run plugin - for later
        """ 
        if "can" in commandPhrase:
            if any(item in commandPhrase for item in self.action_phrases):
                cmd = commandPhrase[2] if commandPhrase[2] in self.action_phrases else None
                
            else:
                cmd = string[len(string) // 2] if string[len(string) // 2] in self.action_phrases else None
                
            if cmd == None:
                print(chr(69)) #Fear the chr(69). It's not an us problem it's a you problem
                raise Exception("Some Vodo magic happened")

            command_list.append("can")
            command_list.append(cmd)
            command_list.append(string[-1]) 
        
        else:
            if any(item in string for item in self.action_phrases):
                cmd = string[:2]
            else:
                print(chr(69)) #Fear the chr(69). It's not an us problem it's a you problem
                raise Exception("Some Vodo magic happened")
            
            string = string[2:]
            command_list.append(cmd[0])
            command_list.append(' '.join(string))

        return command_list