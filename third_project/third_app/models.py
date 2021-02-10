from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    category = models.CharField(max_length=15)
    date_created = models.CharField(max_length=4)

    def __str__(self):
        return self.title
