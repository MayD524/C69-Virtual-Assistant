"""
    Author: Cross/Ryan
    Date : 8/11/2021
    pip install beutifulsoup4
    pip install google

"""
#import bs4
from googlesearch import search


## do stuff with querys
class query_plugin:
    def __init__(self, config:dict) -> None:
        self.config = config

    ## defer between local searches and web searches
    def parse_query(self, args:list) -> None:
        query = args[2]
        search_config = self.config["search_options"]
        print(query)
        for i in search(query = query, 
                        lang  = search_config["lang"],
                        num   = search_config['num'],
                        stop  = search_config['stop'],
                        pause = search_config['pause']):
            print(i)

def plugin_Main(config:dict) -> dict:
    queryPlg = query_plugin(config)
    funcs = {
        "what" : queryPlg.parse_query,
        "where": queryPlg.parse_query,
        "when" : queryPlg.parse_query,
        "how"  : queryPlg.parse_query
    }
    
    return funcs