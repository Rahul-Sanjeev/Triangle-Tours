from django.db import models

# Create your models here.


class Destination(models.Model):
    place_name = models.CharField(max_length=255)
    weather = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    google_map_link = models.URLField(max_length=200)
    image = models.ImageField(upload_to="images/")
    description = models.TextField()

    def __str__(self):
        return self.place_name
