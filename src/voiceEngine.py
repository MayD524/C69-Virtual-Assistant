import pyttsx3
import UPL

class c69_voiceEngine:
    def __init__(self, config:dict) -> None:
        self.config = config["text_to_speech"]
        self.voice_actions  = {
            "say" : self.say,
            "read_lines" : self.read_lines
        }
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', self.engine.getProperty('voices')[self.config["gender"]].id)
        self.engine.setProperty('volume', self.config['volume'])
        #self.engine.setProperty('rate', self.config['rate'])
        
    def say(self, text:str) -> None:
        print(text)
        self.engine.say(text)
        self.engine.runAndWait()
        
    
    def read_lines(self, lines:list) -> None:
        if type(lines) == str:
            self.say(lines)
            return
        
        for line in lines:
            self.say(line)