from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Ad(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    division = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.TextField()
    description = models.TextField()
    room_type = models.CharField(max_length=50)
    images = models.ManyToManyField('AdImage', blank=True)
    phone=models.CharField(max_length=20,null=True)
    date = models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return self.title

class AdImage(models.Model):
    image = models.ImageField(upload_to='ads/images/')



class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')
    alt_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.alt_text or "Banner"

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
