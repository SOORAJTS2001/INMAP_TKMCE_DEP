from django.db import models
from important_pts_tkmce.important_pts import important_points
FROM_CHOICES = []
TO_CHOICES = []
for key in important_points.keys():
    FROM_CHOICES.append((key, key))
    TO_CHOICES.append((key, key))
class ImageModel(models.Model):
    from_field = models.CharField(max_length=100, choices=FROM_CHOICES)
    to_field = models.CharField(max_length=100, choices=TO_CHOICES)
    image_url = models.URLField(default='this is a default value')
    distance = models.FloatField()
