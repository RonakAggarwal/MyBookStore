from django.db import models


# Create your models here.
# Creating Author Model class
class Author(models.Model):
    AuthorName = models.CharField(max_length=30,unique=True)
    PhoneNumber = models.CharField(max_length=15, primary_key=True)
    BirthDate = models.DateField()
    DeathDate = models.DateField()

    def __str__(self):
        return self.AuthorName


# Creating Category Model class
class Category(models.Model):
    CategoryName = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.CategoryName


# Creating Book Model class
class Book(models.Model):
    Title = models.CharField(max_length=50, primary_key=True)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    Publisher = models.CharField(max_length=50)
    PublishDate = models.DateField()
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Price = models.FloatField()
    SoldCount = models.IntegerField()

    def __str__(self):
        return self.Title
