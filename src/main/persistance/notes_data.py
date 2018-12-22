from pymongo import MongoClient

from main.utils.constants import Constants
from main.utils.utilities import get_registered_obj, set_registered_obj

class MongoDBConnection(object):
    def __init__(self):
        config = get_registered_obj(Constants.CONFIGPARSER).config_parser
        host = config[Constants.MONGODB][Constants.MONGOHOST]
        port = int(config[Constants.MONGODB][Constants.MONGOPORT])

        self.connection = MongoClient(host, port)
        
class MongoDataManager(object):
    @staticmethod
    def get_notes(subj_name, term):
        conn = get_registered_obj(Constants.DBCONNECTION).connection

        all_lines = conn.pzone_data.notes.find({Constants.SUBJECT_STR: subj_name})
        for line in all_lines:
            if term in line[Constants.LINE_STR]:
                return line

        return {}

    @staticmethod
    def add_notes(data):
        conn = get_registered_obj(Constants.DBCONNECTION).connection
    
        conn.pzone_data.notes.insert(data)

set_registered_obj(Constants.DBCONNECTION, MongoDBConnection())
