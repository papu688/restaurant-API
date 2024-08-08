from django.db import models

# Create your models here.
class Chef(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    chef = models.ForeignKey(Chef, on_delete = models.CASCADE)

    def __str__(self):
        return self.title