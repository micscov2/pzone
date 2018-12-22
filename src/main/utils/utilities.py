import configparser

from main.utils.constants import Constants


class Registry(object):
    entries = {}

    def __init__(self):
        Registry.entries[Constants.DBCONNECTION] = None
        Registry.entries[Constants.CONFIGPARSER] = None

class PzoneConfigParser(object):
    def __init__(self, filename):
        self.config_parser = configparser.ConfigParser()
        self.config_parser.read(filename)

def filter_only_real_aphab(input_str):
    input_str = input_str.replace("\n", "")
    input_str = input_str.replace("\t", "")

    return input_str

def get_registered_obj(name):
    return Registry.entries.get(name)

def set_registered_obj(name, value):
    if Registry.entries.get(name) is None:
        Registry.entries[name] = value

set_registered_obj(Constants.CONFIGPARSER, PzoneConfigParser("../pzone.properties"))
