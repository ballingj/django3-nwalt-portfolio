# Two simple steps to include the Project database
# 1) import the data in the Project database
# 2) add Project.objects.all() method in the home function
#
from django.shortcuts import render
from .models import Project

print(Project.objects.all())

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})
