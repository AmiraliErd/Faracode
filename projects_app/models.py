from django.db import models

class project(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=35)
    address = models.CharField(max_length=140, null=True, blank=True)
    image = models.ImageField(null=True, upload_to='projects')

    def __str__(self):
        return self.title


# Create your models here.
