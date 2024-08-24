from django.db import models


class Student(models.Model):
    """Model for storing information about students"""

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    image = models.ImageField()
    file = models.FileField()


class Product(models.Model):
    pass


# Reference : https://docs.djangoproject.com/en/5.0/topics/db/models/
# Reference : https://docs.djangoproject.com/en/5.0/topics/migrations/
"""
    makemigrations : These command creates a state with all changes need to br applied
                        to the database and whenever a new migration is generated, these 
                        command runs all the migrations internally and match with the
                        migrations available in the database.
    
    migrate : This command runs all the migrations and applies them to the database.
    
    One more important thing is that the django also stores all the migrations
    in the database also to keep track of the migration, if we delete any migration
    files it will throw an exception about the migration.
"""