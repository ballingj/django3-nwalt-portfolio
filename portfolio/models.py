# ImageField will require install of Pillow # "pip install pillow"
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        """ displays the title as an object in the Admin Page instead of 'Project object (n)' """
        return str(self.title)