from django.db import models

from django.contrib.auth.models import User

# class Article(models.Model):
#    name = models.CharField(max_length=64)
#    text = models.TextField()
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    create = models.DateTimeField()

#    def __str__(self):
#        return self.name


class Author(models.Model):
   name = models.CharField(max_length=32)
   birthday_year = models.PositiveIntegerField()

   def __str__(self):
       return self.name


class Biography(models.Model):
   text = models.TextField()
   author = models.OneToOneField(Author, on_delete=models.CASCADE)


class Book(models.Model):
   name = models.CharField(max_length=32)
   authors = models.ManyToManyField(Author)


class Article(models.Model):
   name = models.CharField(max_length=32)
   author = models.ForeignKey(Author, models.PROTECT)