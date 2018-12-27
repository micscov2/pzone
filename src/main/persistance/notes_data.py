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

        all_lines = conn.pzone_data.notes.find(
                            {Constants.SUBJECT_STR: subj_name},
                            projection={'_id': False, 'subject': False}
                    )

        desired_lines = []
        for line in all_lines:
            if term in line[Constants.LINE_STR]:
                desired_lines.append(line)

        return desired_lines

    @staticmethod
    def add_notes(data):
        conn = get_registered_obj(Constants.DBCONNECTION).connection

        seq_obj = conn.pzone_data.counter_pzone.find_and_modify(
                        query={'_id': 'item_id'}, 
                        update={'$inc': {'sequence_value': 1}})    
        data['_id'] = int(seq_obj['sequence_value'])

        conn.pzone_data.notes.insert(data)

set_registered_obj(Constants.DBCONNECTION, MongoDBConnection())
