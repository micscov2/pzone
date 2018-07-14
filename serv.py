import os
import sys
from flask import Flask, request
import datetime
from flask_cors import cross_origin
import json

ep = datetime.datetime(1970,1,1,0,0,0)

def get_matching_line(user_input):
    output = {}
    num = 0
    row = 0
    for root, folder, filelist in os.walk("data"):
        for filename in filelist:
            filename = root + "/" + filename
            with open(filename) as fr:
                file_data = fr.read().lower()
                try:
                    if user_input in file_data:
                        file_data_arr = file_data.split("\n")
                        for line_data in file_data_arr:
                            if user_input in line_data:
                                output[str(num) + " " + line_data] = filename + " " + str(row)
                                row += 1
                                num += 1
                except UnicodeDecodeError:
                    import pdb; pdb.set_trace()
    return num, output

app = Flask(__name__)

@app.route("/catalogue/search/<user_input>")
@cross_origin()
def catalogue_search_data(user_input):
    print(user_input)
    num, res = get_matching_line(user_input)
    print("Number of records: {}".format(num))
    return json.dumps(res)

@app.route("/catalogue/addNew", methods=["POST"])
@cross_origin()
def catalogue_add_data():
    print(json.dumps(request.data))
    output_data = ""
    filename = str((datetime.datetime.utcnow()- ep).total_seconds()) + ".txt"
    for entry in request.data[1:-1].split(","):
        key, value = entry.split(":")
        key = key[1:-1]
        value = value[1:-1]
        if key != "filename": 
            output_data += (value + "\n")
        else:
            if value != "SYSTEM_TAKEN":
                filename = value
    with open("data/fx/" + filename, "w") as fw:
        fw.write(output_data)
    return json.dumps({"Result": "OK"})

@app.route("/catalogue/addBookmarks", methods=["POST"])
@cross_origin()
def catalogue_add_bookmarks():
    output_data = ""
    for entry in request.data.split('","')[1:-1]:
        output_data += (entry + "\n")
    with open("bookmarks/bookmarks.txt", "w") as fw:
        fw.write(output_data)
    return json.dumps({"Result": "OK"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7880)
