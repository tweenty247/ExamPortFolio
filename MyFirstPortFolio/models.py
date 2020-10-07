from django.db import models


class DataName(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.IntegerField()
    text = models.TextField()

    def __str__(self):
        return self.name


