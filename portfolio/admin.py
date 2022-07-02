from django.contrib import admin

# Register your models here.
from .models import Project


# add the model that we want to see in admin
admin.site.register(Project)
