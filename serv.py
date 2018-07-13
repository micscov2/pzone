from flask import Flask, request
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='/Users/parkhan/Code/Github/pzone')

@app.route('/')
def some_func1():
    return app.send_static_file('main.html')

if __name__ == "__main__":
    app.run()
