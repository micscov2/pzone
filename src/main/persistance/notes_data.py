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
    def get_notes(**kwargs):
        conn = get_registered_obj(Constants.DBCONNECTION).connection

        return conn.pzone_data.notes.find_one()

set_registered_obj(Constants.DBCONNECTION, MongoDBConnection())
