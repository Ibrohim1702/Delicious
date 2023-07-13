from django.db import models


# Create your models here.
class Category(models.Model):
    content = models.CharField(max_length=56)
    slug = models.SlugField(max_length=56, null=True, blank=True)
    img = models.ImageField()

    def __str__(self):
        return self.content


class Recipe(models.Model):
    name = models.CharField(max_length=256)
    date = models.DateField(auto_now_add=True)
    img = models.ImageField()
    rate = models.IntegerField()
    prep = models.IntegerField()
    cook = models.IntegerField()
    yields = models.IntegerField()
    step = models.TextField()
    ingredients = models.TextField()
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.rate} {self.name}"


class Suggestion(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    subject = models.CharField(max_length=128)
    message = models.TextField()

    def __str__(self):
        return self.name
