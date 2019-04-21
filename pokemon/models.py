from django.db import models

class Pokemon(models.Model):
    pokemon_name = models.CharField(max_length=255)
    type_primary = models.CharField(max_length=255)
    type_secondary = models.CharField(max_length=255, blank=True)
    height = models.IntegerField(default=0)
    height_units = models.CharField(max_length=10, default="inches")
    weight = models.IntegerField(default=0)
    weight_units = models.CharField(max_length=10, default="lbs")
    pokedex_number = models.IntegerField(primary_key=True)
    pokemon_image = models.URLField(blank=True)
