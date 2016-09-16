from models import MarkerModel
from objects import MarkerClass
import requests
import json

def get_data_from_API():

    url = "https://opendurham.nc.gov/api/records/1.0/search/"
    parameters = {"dataset": "nc-historic-road-markers", "rows": "6028"}

    response = requests.post(url, parameters)

    the_dict = json.loads(response.text)

    return the_dict

def create_marker_model_list(the_dict):

    marker_list = []

    for key, value in the_dict['records'].items():
        marker = MarkerClass(value)
        marker_list.append(marker)

    return marker_list

marker_dictionary = get_data_from_API()
marker_model_list = create_marker_model_list(marker_dictionary)
