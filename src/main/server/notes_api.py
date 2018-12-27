import json

from flask import Blueprint, request, Response
from flask_cors import cross_origin

from main.persistance.notes_data import MongoDataManager
from main.utils.utilities import filter_only_real_aphab
from main.utils.constants import Constants

notes_apis = Blueprint('notes_apis', __name__)

@notes_apis.route('/search/<subj_name>')
@cross_origin()
def get_notes(subj_name):
    term = request.args.get('term') 

    return json.dumps(MongoDataManager.get_notes(subj_name, term))
    
@notes_apis.route('/add', methods=['POST'])
def add_notes():
    data = request.get_json()
    data[Constants.LINE_STR] = filter_only_real_aphab(data[Constants.LINE_STR])
    MongoDataManager.add_notes(data)

    return "{'status': 'ok'}"

__all__ = (notes_apis, )
