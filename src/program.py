import json
import sys

sys.path.insert(0, "/utils")
from parseTime import parseTime

# get json file data
with open('../data.json', 'r') as e:
    data = json.loads(e.read())

parsed_time = parseTime("23:12:10")

print("Hour - ", parsed_time.hour, "\nMinute - ", parsed_time.minute)