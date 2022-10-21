from dataclasses import asdict
import json
import sys

sys.path.insert(0, '../utils')
from parseTime import parse_time
from createBreaks import create_breaks

# get json file data
with open('../data.json', 'r') as e:
    data = json.loads(e.read())

parsed_time = parse_time("23:12:00")

print("Parsed time - ", parsed_time, "\nDuration - ", "15")
print("Break - ", create_breaks(parsed_time, "15"))


