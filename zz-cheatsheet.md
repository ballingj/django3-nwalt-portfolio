
### Setup for virtual environment
>create a virtual environment: install a package that allows to create a virtual environment
```sh
pip install virtualenv
```
>  now create a virtual environment with command `virtualenv <name>` : here we are naming it `env`
>  this will create a new folder after the name you provided
```sh
virtualenv env
```
### Activate the virtual environment
>you should see (env) in the front of prompt
```sh
source ./env/bin/activate
```
### Activate for Windows
```sh
env\scripts\activate
```
### When done - Deactivate
```sh
deactivate
```
#### Deactivate for Windows
```sh
env\scripts\deactivate
```

### go back to virtual env - Install Django 
```sh
pip install django
```
> NOTE:  Install packages while in the virtual environment to avoid installing in global settings

# More Commands

### general help
```sh
django-admin help
```
### start a project
```sh
django-admin startproject <name_of_project>
```

### Ex:  start a project 'project_name' in current directory
> Don't forget the period at the end
```sh
django-admin startproject project_name .   
```
### run server
```sh
python manage.py runserver
```

### fix linter pylint if not installed
shift + ctrl + 'p'  > select interpreter for env
```sh
install pylint
```
### add the first app in current project
```sh
python manage.py startapp <name_of_app>
```
### Ex: add "app_name" app 
```sh
python manage.py startapp app_name
```

> Note: Below is required step everytime you add an app:
- Go to settings.py in main project and add the new app 
- Add the class name included in the Apps.py in the INSTALLED_APPS list

```sh
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'portfolio',
]
```
## Working with Models

### Create a model
> exaple model
> Models Field Reference: https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.ImageField
```
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
```

### Make Migrations
> makemigrations is responsible for creating new migrations based on the changes you have made to your models.
> Basically, you need to make the migration files whenever models are modified.
```sh
python manage.py makemigrations
```

### Migrate
> migrate is responsible for applying and unapplying migrations.  Applies the migration files created by make migrations, including the initial migrations pending after a project is created (i.e. admin app).
```sh
python manage.py migrate
```

### Create Superuser for /admin directory
```sh
python manage.py createsuperuser
```

### Change password for user 
```sh
python manage.py changepassword username
```