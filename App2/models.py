from django.db import models

# Create your models here.

class Planet(models.Model):
    planet_id = models.AutoField(primary_key=True)
    planet_title = models.CharField(max_length=200, null=True, blank=True)
    planet_text = models.TextField(max_length=1000, null=True, blank=True)
    planet_image = models.ImageField(upload_to="planet", null=True, blank=True)

    def __str__(self):
        return f"{self.planet_title}"