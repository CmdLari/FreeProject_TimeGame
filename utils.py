import json


class Utils:
    '''Reads and writes to json-File'''

    @staticmethod
    def write_to_playerstate(json_key: str, value: int, json_path: str):
        '''Write value based on given json key into json file.'''
        
        with open(json_path, "r") as json_file:
            playerstats = json.load(json_file)

            playerstats[json_key] = value

        with open(json_path, "w") as json_file:
            json.dump(playerstats, json_file, indent=4)

    @staticmethod
    def read_from_playerstate(json_key: str, json_path: str) -> int:
        '''Reads value from json file with a given key.'''
        
        with open(json_path, "r") as json_file:
            playerstats = json.load(json_file)

            return playerstats[json_key]
