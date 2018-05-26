from django.db import models

# Create your models here.
class Note(models.Model):
    Title = models.CharField(max_length=50)
    Data = models.CharField(max_length=250)
    Date = models.DateField()

    def __str__(self):
        return self.Title