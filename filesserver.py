import os
import sys
from flask import Flask
from flask_cors import cross_origin

def get_matching_line(user_input):
    for root, folder, filelist in os.walk("data"):
        for filename in filelist:
            filename = root + "/" + filename
            with open(filename) as fr:
                file_data = fr.read().lower()
                if user_input in file_data:
                    file_data_arr = file_data.split("\n")
                    for line_data in file_data_arr:
                        if user_input in line_data:
                            return filename + ":->:" + line_data

app = Flask(__name__)

@app.route("/catalogue/search/<user_input>")
@cross_origin()
def catalogue_search_data(user_input):
    print(user_input)
    return get_matching_line(user_input)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7880)
