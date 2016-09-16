"""This is a test file for playing around with communicating with the API."""

import requests
import json

url = "https://opendurham.nc.gov/api/records/1.0/search/"
parameters = {"dataset": "nc-historic-road-markers", "rows": "6028"}

response = requests.post(url, parameters)
print(dir(response))
print(response.text)

the_dict = json.loads(response.text)
# with open('dumpfile.json', 'w') as outfile:
#     json.dump(the_dict, outfile)

key = the_dict['records']
print(type(the_dict))
# for key, value in the_dict.items():
#     print('type: ', type(value))
#     for i in value:
#         count += 1
