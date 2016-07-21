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
    sketch = models.CharField() #no max length?
    x_coord = models.FloatField()
    object_id = models.IntegerField()

      # 
    #   "records.0.recordid": "c2eee1f2e6f4c89df01262cbb00da0fbb6369eda",
    #   "records.0.record_timestamp": "2016-07-15T13:00:20+00:00",
    #   "records.0.datasetid": "nc-historic-road-markers",
    #   "records.0.fields.id": "I-75",
    #   "records.0.fields.yearcast": "1961-P",
    #   "records.0.fields.geo_point_2d.0": 35.23298300017134,
    #   "records.0.fields.geo_point_2d.1": -78.67858899988092,
    #   "records.0.fields.suffix": 75,
    #   "records.0.fields.countyid": 26,
    #   "records.0.fields.geo_shape.type": "Point",
    #   "records.0.fields.geo_shape.coordinates.0": -78.67858899988092,
    #   "records.0.fields.geo_shape.coordinates.1": 35.23298300017134,
    #   "records.0.fields.location": "NC 82 north of Godwin",
    #   "records.0.fields.markertextwithbreaks": "The 1865 home of Wm. Smith,\r\n100 yds. E., was used as a\r\nhospital for Union troops in\r\nthe Battle of Averasboro,\r\nMarch 15-16, 1865.",
    #   "records.0.fields.buffer": 1,
    #   "records.0.fields.maintermnonpermutated": "FEDERAL HOSPITAL",
    #   "records.0.fields.markertitle": "FEDERAL HOSPITAL",
    #   "records.0.fields.markertext": "The 1865 home of Wm. Smith, 100 yds. E., was used as a hospital for Union troops in the Battle of Averasboro, March 15-16, 1865.",
    #   "records.0.fields.dotdistrictid": 6,
    #   "records.0.fields.mainterm": "FEDERAL HOSPITAL",
    #   "records.0.fields.gps": "Y",
    #   "records.0.fields.uniquekey": 53365,
    #   "records.0.fields.ycoord": 35.232983,
    #   "records.0.fields.prefix": "I",
    #   "records.0.fields.requestor": "Staff",
    #   "records.0.fields.sketch": "On March 15th the left wing of General Sherman’s Union army, commanded by General [H. W. Slocum, H-60], was advancing along the road from Fayetteville to Averasboro. General H. J. Kilpatrick’s cavalry division was in the lead, skirmishing with General Joseph Wheeler’s Confederate cavalry which contested the Union advance. \r\n\r\n\tAt 3:00 P.M. the Union forces struck a heavy Confederate skirmish line. General Smith Atkins’ 9th Michigan cavalry drove the skirmishers back into the first of three lines of breastworks erected across the road. The Union cavalry then constructed heavy barricades in front of the Confederate works.  Nearly three hours after the initial Union attack began, Confederate General [W. B. Taliaferro, I-72], whose division was holding position, ordered an attack along his line. The Union forces, though hard-pressed, were able to hold their position due to the arrival of reinforcements from the 14th Corps. Nightfall found the two armies in nearly the same positions they had held throughout the afternoon. General [W. T. Sherman, HHH-1], Union commander, arrived on the field during the night. \r\n\r\n\tAt 6:00 A.M. on March 16th, the Union forces attacked Taliaferro’s line, driving the Confederates before them. Then the Southerners launched a desperate counter-attack. A disaster for the Union forces was averted when portions of the 20th Corps arrived upon the field. Three batteries of artillery were placed in the position near the [John Smith house, I-74]. They began firing upon the Confederates, driving them back into their breastworks. \r\n\r\n\tWithin five hours two newly-arrived Union brigades engaged the Confederates in front, while the brigade of Colonel Henry Case assaulted the Confederate right flank. The attack forced the Confederates to withdraw into their [second line of works, H-98]. \r\nUnion General H. J. Kilpatrick’s cavalry found a back road and circled to the rear of the Confederate position. The Union cavalry attempted to use the road to flank the Confederates, but was stopped by Colonel G. P. Harrison’s brigade of McLaws’ division after moving only a short distance. \r\n\r\n\tGeneral Taliaferro decided to abandon the Confederate second position after finding his men in danger of being flanked. At 1:00 P.M. he withdrew to the third and final line of earthworks, where he was assisted by McLaw’s division on his left and Wheeler’s dismounted cavalry on his right. [Rhett’s disorganized brigade, I-71] was held in general reserve behind the junction of this road and the Smithfield road. \r\n\r\n\tThe Union forces soon advanced and established a strong line immediately in front of the Confederate third line. From the new position they pressed the Confederates all afternoon and part of the evening, but were unable to break the line. At 8:00 P.M. General W. J. Hardee, commanding the Confederate forces at Averasboro, having accomplished his objectives, began withdrawing his corps along the Smithfield road. Wheeler’s cavalry was left behind to cover the retreat. By 4:00 A.M. on March 17th, all Confederate units had been withdrawn, leaving the Union forces in control.  Nearly 700 Union soldiers and approximately 500 Confederates had been killed or wounded.  Local farms including [“Oak Grove”, I-73] and [“Lebanon”, H-97] as well as several other smaller dwellings were utilized by both armies as field hospitals. \r\n\r\n\tGeneral Hardee wished to accomplish two things by contesting the Union advance at Averasboro. The first objective was to determine for General Joseph E. Johnston, commander of all Confederate forces in the Carolinas, whether Sherman’s army was advancing on Raleigh or Goldsboro. The Confederates learned it was moving on Goldsboro. The second objective was to stretch out the distance between Sherman’s left and right wings (which were moving on parallel roads) in order to give General Johnston a chance to concentrate his smaller army and destroy the Union left wing before the right wing could come to its assistance. Both of these objectives were fully accomplished. The stage was now set for the greater [Battle of Bentonville, HH-1] fought 25 miles east on March 19-21, 1865. \r\n\r\n\r\nReferences:\r\nMark L. Bradley, <i>Last Stand in the Carolinas:  The Battle of Bentonville</i> (1996)\r\nMark A. Moore, <i>Moore’s Historical Guide to the Battle of Bentonville</i> (1997)\r\nJohn G. Barrett, <i>Sherman’s March through the Carolinas</i> (1956)\r\nWilson Angley, Jerry L. Cross, and Michael Hill, <i>Sherman’s March through North Carolina:  A Chronology</i> (1995)\r\nAverasboro Battlefield Commission website:  http://www.averasboro.com/",
    #   "records.0.fields.xcoord": -78.678589,
    #   "records.0.fields.notes": "Returned to foundry for cap repair, 3/01.",
    #   "records.0.fields.objectid": 925,
    #   "records.0.fields.markerid": "I-75",
    #   "records.0.geometry.type": "Point",
    #   "records.0.geometry.coordinates.0": -78.67858899988092,
    #   "records.0.geometry.coordinates.1": 35.23298300017134,
