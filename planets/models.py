from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=50, unique=True)
    climate = models.CharField(max_length=50)
    terrain = models.CharField(max_length=50)
    films_apparitions = models.IntegerField()

    def __str__(self) -> str:
        return self.name
