from django.db import models

# Create your models here.
class MarkerModel(models.Model):

    recordid = models.CharField(max_length=50)
    record_timestamp = models.CharField(max_length=50)
    field_id = models.CharField(max_length=50)
    field_yearcast = models.CharField(max_length=50)
    field_geo_point_2d_0 = models.FloatField()
    field_geo_point_2d_1 = models.FloatField()
    field_countyid = models.IntegerField()
    geoshape_type = models.CharField(max_length=50)
    geoshape_coord_0 = models.FloatField()
    geoshape_coord_1 = models.FloatField()
    field_location = models.CharField(max_length=50)
    marker_title = models.CharField(max_length=50)
    marker_text = models.CharField(max_length=500)
    main_term = models.CharField(max_length=50)
    gps = models.CharField(max_length=1, default='N')
    unique_key = models.CharField(max_length=50)
    y_coord = models.FloatField()
    sketch = models.TextField() #no max length?
    x_coord = models.FloatField()
    object_id = models.IntegerField()
