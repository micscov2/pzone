from flask import Blueprint, request

from main.persistance.notes_data import MongoDataManager

search_apis = Blueprint('search_apis', __name__)

@search_apis.route('/<subj_name>')
def get_notes(subj_name):
    term = request.args.get('term') 

    return str(MongoDataManager.get_notes())

__all__ = (search_apis, )
