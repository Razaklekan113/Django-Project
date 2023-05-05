from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    mobile = models.IntegerField()

    def __str__(self):
        return self.name
