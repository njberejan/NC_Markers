class MarkerClass:

    def __init__(self, dictionary):
        """ dictionary should be response culled to records dict, first key = record number """
        for key, value in dictionary.items():
            if dictionary.get('fields') is None:
                raise Exception('This record has no fields data')

            else:

                self.recordid = dictionary[key]['recordid']
                self.record_timestamp = dictionary[key]['record_timestamp']
                self.field_id = dictionary[key]['fields']['id']
                self.field_yearcast = dictionary[key]['fields']['yearcast']
                self.field_geo_point_2d_0 = dictionary[key]['fields']['geo_point_2d']['0']
                self.field_geo_point_2d_1 = dictionary[key]['fields']['geo_point_1d']['1']
                self.field_countyid = dictionary[key]['fields']['countyid']
                self.geoshape_type = dictionary[key]['fields']['geo_shape']['type']
                self.geoshape_coord_0 = dictionary[key]['fields']['geo_shape']['coordinates']['0']
                self.geoshape_coord_1 = dictionary[key]['fields']['geo_shape']['coordinates']['1']
                self.field_location = dictionary[key]['fields']['location']
                self.marker_title = dictionary[key]['fields']['markertitle']
                self.marker_text = dictionary[key]['fields']['markertext']
                self.main_term = dictionary[key]['fields']['mainterm']
                self.gps = dictionary[key]['fields']['gps']
                self.unique_key = dictionary[key]['fields']['uniquekey']
                self.sketch = dictionary[key]['fields']['sketch']
                self.x_coord = dictionary[key]['fields']['xcoord']
                self.y_coord = dictionary[key]['fields']['ycoord']
                self.object_id = dictionary[key]['fields']['objectid']
