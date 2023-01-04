from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    project_url = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=1000)