import pyttsx3
import UPL

class c69_voiceEngine:
    def __init__(self, config:dict) -> None:
        self.config = config["text_to_speech"]
        
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', self.engine.getProperty('voices')[self.config["gender"]].id)
        self.engine.setProperty('volume', self.config['volume'])
        self.engine.setProperty('rate', self.config['rate'])
        
    def say(self, text:str) -> None:
        self.engine.say(text)
        self.engine.runAndWait()