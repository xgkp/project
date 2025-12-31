from django.db import models

class NewBook(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    published_date = models.DateField(auto_now_add=True)
    price = models.FloatField(default=0.0)
