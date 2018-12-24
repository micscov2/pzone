from pymongo import MongoClient

conn = MongoClient("localhost", 27017)

all_data = conn.pzone_data.notes.find({"subject": "indian_history"})
uniq_words = {}

for data in all_data:
    line = data["line"]
    for word in line.split(" "):
        uniq_words[word] = 1

print(len(uniq_words.keys()))
