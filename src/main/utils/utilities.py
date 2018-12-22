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


if Registry.entries.get(Constants.CONFIGPARSER) is None:
    Registry.entries[Constants.CONFIGPARSER] = PzoneConfigParser("pzone.properties")
