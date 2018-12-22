from flask import Blueprint, request

search_apis = Blueprint('search_apis', __name__)

@search_apis.route('/<subj_name>')
def get_notes(subj_name):
    term = request.args.get('term') 

    return "Garbled data!"

__all__ = (search_apis, )
