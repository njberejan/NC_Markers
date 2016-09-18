from django.db import models

# Create your models here.
class MarkerModel(models.Model):

    recordid = models.TextField()
    record_timestamp = models.CharField(max_length=255)
    field_id = models.CharField(max_length=255)
    field_yearcast = models.CharField(max_length=255)
    field_geo_point_2d_0 = models.FloatField()
    field_geo_point_2d_1 = models.FloatField()
    field_countyid = models.IntegerField()
    geoshape_type = models.CharField(max_length=255)
    geoshape_coord_0 = models.FloatField()
    geoshape_coord_1 = models.FloatField()
    field_location = models.CharField(max_length=255)
    marker_title = models.TextField()
    marker_text = models.TextField()
    main_term = models.CharField(max_length=255)
    gps = models.CharField(max_length=255, default='N')
    unique_key = models.CharField(max_length=255)
    y_coord = models.CharField(max_length=255)
    sketch = models.TextField() #no max length?
    x_coord = models.CharField(max_length=255)
    object_id = models.IntegerField()
