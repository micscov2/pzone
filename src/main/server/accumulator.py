from flask import Flask
from notes_api import notes_apis

app = Flask('accumulator-pzone')

app.register_blueprint(notes_apis, url_prefix='/pzone/v1')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7880)
