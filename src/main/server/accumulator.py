from flask import Flask
from search_api import search_apis

app = Flask('accumulator-pzone')

app.register_blueprint(search_apis, url_prefix='/search')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7880)
