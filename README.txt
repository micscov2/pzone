# pzone

Guarantee
---------
Search in 10,000,000 notes with un-noticeable delay

Components
----------
. MongoDB (for data)
. Redis (for logging)

# Don't forget to export src directory into PYTHONPATH
export PYTHONPATH="<some_directory>"

# To maintain uniqueness of records one counter is maintained
# in MongoDB (as out of box it does not give one)
# > db.counter_pzone.find()
# { "_id" : "item_id", "sequence_value" : 44 }

