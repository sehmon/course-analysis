import json
import datetime
from nuapiclient import NorthwesternAPIClient
from config import api_key

client = NorthwesternAPIClient(api_key);
terms = client.terms()

current_term = terms[0]
print(current_term['id'])

subjects = client.subjects()
courses = []
courses.append(str(datetime.datetime.now().date()))
i = 0.0;

for sub in subjects:
    print("Getting courses for {}, {}% complete".format(sub['name'], 100*round(i/(len(subjects)-1), 2)))
    courses.extend(client.courses_details(term=current_term['id'], subject=sub['symbol']))
    i+= 1
filename = "{}:{}".format(str(current_term['id']), str(datetime.datetime.now().date()))

with open(filename+".json", 'w') as outfile:
    json.dump(courses, outfile)
