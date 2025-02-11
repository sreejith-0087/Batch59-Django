from django.db import models

# Create your models here.


class Details(models.Model):
    Name = models.CharField(max_length=30)
    Age = models.IntegerField()
    Subject = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


