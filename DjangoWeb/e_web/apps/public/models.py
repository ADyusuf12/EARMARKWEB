from django.db import models

class Properties_Listing(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    parking_space = models.IntegerField(null=True)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    sqm = models.IntegerField()
    address = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.CharField(max_length=500)
    # video = models.FileField()
    google_map = models.CharField(max_length=500)
    status = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title