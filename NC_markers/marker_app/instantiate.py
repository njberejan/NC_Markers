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

def save_models_to_database():

    marker_dictionary = get_data_from_API()
    marker_model_list = create_marker_model_list(marker_dictionary)
    for marker in marker_model_list:
        marker_model = MarkerModel(
            recordid = marker.recordid,
            record_timestamp = marker.record_timestamp,
            field_id = marker.field_id,
            field_yearcast = marker.field_yearcast,
            field_geo_point_2d_0 = marker.field_geo_point_2d_0,
            field_geo_point_2d_1 = marker.field_geo_point_2d_1,
            field_countyid = marker.field_countyid,
            geoshape_type = marker.geoshape_type,
            geoshape_coord_0 = marker.geoshape_coord_0,
            geoshape_coord_1 = marker.geoshape_coord_1,
            field_location = marker.field_location,
            marker_title = marker.marker_title,
            marker_text = marker.marker_text,
            main_term = marker.main_term,
            gps = marker.gps,
            unique_key = marker.unique_key,
            y_coord = marker.y_coord,
            sketch = marker.sketch,
            x_coord = marker.x_coord,
            object_id = marker.object_id,    
        )
        marker_model.save()
