import requests
import sys

if len(sys.argv) < 3:
    print("Please enter filename, and subject name")
    sys.exit(1)

filename = sys.argv[1]
subj_name = sys.argv[2]

with open(filename) as fp:
    for lines in fp.readlines():
        if len(lines) > 2:
            for line in lines.split("."):
                line = line.replace('"', 'DOUBLE_QUOTE').replace("'", 'SINGLE_QUOTE')
                requests.post("http://localhost:7880/pzone/v1/add", json={
                            "subject": subj_name,
                            "line": line
                            }
                        )
