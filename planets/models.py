from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=50, unique=True)
    climate = models.CharField(max_length=50)
    terrain = models.CharField(max_length=50)
    number_apparitions = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name
        