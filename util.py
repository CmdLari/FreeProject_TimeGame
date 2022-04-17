from ctypes import Union
import json

class Util:
    """ Utility class for common functions """

    @staticmethod
    def write_to_save(json_key: str, value: int, json_path: str):
        """ Writes a value to a json-file.
        
        Args:
            json_key (str): The key to write to.
            value (int): The value to write.
            json_path (str): The path to the json-file.
        """        
        with open(json_path, "r") as json_file:
            save = json.load(json_file)

            save[json_key] = value

        with open(json_path, "w") as json_file:
            json.dump(save, json_file, indent=4)

    @staticmethod
    def read_from_save(json_key: str, json_path: str) -> Union[int, str]:
        """Reads value based on given json key from json file.
        
        Args:
            json_key (str): The key to read from the json file.
            json_path (str): The path to the json file.

        Returns:
            Union[int, str]: The value of the given key.
        """
        with open(json_path, "r") as json_file:
            save = json.load(json_file)
            return save[json_key]