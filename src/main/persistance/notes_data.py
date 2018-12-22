from pymongo import MongoClient

from main.utils.constants import Constants
from main.utils.utilities import Registry

class MongoDBConnection(object):
    def __init__(self):
        self.connection = MongoClient('localhost', 27017)
        
class MongoDataManager(object):
    def __init__(self):
        pass

    def get_notes(self):
        conn = Registry.entries[Constants.DBCONNECTION].connection  
        return conn.pzone_data.notes.find_one()

if Registry.entries.get(Constants.DBCONNECTION) is None:
    Registry.entries[Constants.DBCONNECTION] = MongoDBConnection()

print (MongoDataManager().get_notes())
