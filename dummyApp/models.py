from django.db import models

# Create your models here.
class KirrURL(models.Model):
    url = models.CharField(max_length=220,)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        print("something")
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = code_generator()
        #super(KirrURL, self).save()
    
    def __str__(self):
        return str(self.url)
    