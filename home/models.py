
# Create your models here.
from django.db import models
from geopy.geocoders import Nominatim
class Service(models.Model):
    image = models.ImageField(upload_to='service_images/')
    name = models.CharField(max_length=255)
    description = models.TextField()
    

    def __str__(self):
        return self.name

class SpaCenter(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    contact_number = models.CharField(max_length=20)
    banner_image = models.ImageField(upload_to='spa_center/banner_images/')
    spa_logo = models.ImageField(upload_to='spa_center/spa_logos/')
    owner_name = models.CharField(max_length=255)
    email = models.EmailField()
    whatsapp_contact = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20)
    address = models.TextField()
    services = models.ManyToManyField(Service, related_name='spa_center_services')
    gallery_image1 = models.ImageField(upload_to='spa_center/gallery_images/')
    gallery_image2 = models.ImageField(upload_to='spa_center/gallery_images/')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.latitude or not self.longitude:
            geolocator = Nominatim(user_agent="core")
            location = geolocator.geocode(self.address)
            if location:
                self.latitude = location.latitude
                self.longitude = location.longitude
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

   
