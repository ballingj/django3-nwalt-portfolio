from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_published = models.DateField()

    def __str__(self):
        """ displays the title as an object in the Admin Page instead of 'Blog object (n)' """
        return self.title
