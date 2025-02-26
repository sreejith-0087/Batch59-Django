from django.db import models

# Create your models here.


class Details(models.Model):
    Name = models.CharField(max_length=30)
    Age = models.IntegerField()
    Subject = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class UserModel(models.Model):
    Name = models.CharField(max_length=30)
    Age = models.IntegerField()
    Subject = models.CharField(max_length=50)
    Email = models.EmailField()

    def __str__(self):
        return self.Name


class InfoModel(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Address = models.CharField(max_length=40)
    Phone = models.IntegerField()

    def __str__(self):
        return self.Name


class RegisterModel(models.Model):
    Name = models.CharField(max_length=30)
    Phone = models.IntegerField()
    Email = models.EmailField()
    Password = models.CharField(max_length=25)

    def __str__(self):
        return self.Name


class FileModel(models.Model):
    FileName = models.CharField(max_length=50)
    File = models.ImageField()

    def __str__(self):
        return self.FileName


class Author(models.Model):
    Name = models.CharField(max_length=30)
    #Other Fields
    def __str__(self):
        return self.Name

class Genre(models.Model):
    genre = models.CharField(max_length=30)
    # Other Fields
    def __str__(self):
        return self.genre

class BookModel(models.Model):
    Title = models.CharField(max_length=50)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    Genre = models.ManyToManyField(Genre)
    Published_Date = models.DateField()
    Image = models.ImageField(upload_to='Books/', null=True, blank=True)

    def __str__(self):
        return self.Title

