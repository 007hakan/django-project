from django.db import models
from datetime import datetime
# Create your models here.
class Satici(models.Model):
    header = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField(blank=True,verbose_name='Fotograf ekle')
    created_date = models.DateTimeField(default = datetime.now,blank=True)
    def __str__(self):
        return self.header
    
    
