from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    rating = models.FloatField()
    poster = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.title
