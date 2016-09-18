class MarkerClass:

    def __init__(self, dictionary):
        """ dictionary should be response culled to records dict, first key = record number """
        # for key, value in dictionary.items():
            # if dictionary.get('fields') is None:
            #     raise Exception('This record has no fields data')
            #
            # else:

        # self.recordid = dictionary[key]['recordid']
        # self.record_timestamp = dictionary[key]['record_timestamp']
        self.field_id = dictionary.get('id', 'No ID')
        self.field_yearcast = dictionary.get('yearcast', 'No Year Cast Data')
        self.field_geo_point_2d_0 = dictionary['geo_point_2d'][0]
        self.field_geo_point_2d_1 = dictionary['geo_point_2d'][1]
        self.field_countyid = dictionary.get('countyid', 'NO COUNTY ID')
        self.geoshape_type = dictionary.get('geo_shape', 'NO GEOSHAPE TYPE')
        self.geoshape_coord_0 = dictionary['geo_shape']['coordinates'][0]
        self.geoshape_coord_1 = dictionary['geo_shape']['coordinates'][1]
        self.field_location = dictionary.get('location', 'NO LOCATION')
        self.marker_title = dictionary.get('markertitle', 'NO MARKER TITLE')
        self.marker_text = dictionary.get('markertextwithbreaks', 'NO MARKER TEXT')
        self.main_term = dictionary.get('mainterm', 'NO MAIN TERM')
        self.gps = dictionary.get('gps', 'NO GPS DATA')
        self.unique_key = dictionary.get('uniquekey', 'NO UNIQUE KEY')
        self.sketch = dictionary.get('sketch', 'NO SKETCH')
        self.x_coord = dictionary.get('xcoord', 'NO X COORD')
        self.y_coord = dictionary.get('ycoord', 'NO Y COORD')
        self.object_id = dictionary.get('objectid', 'NO OBJECT ID')
