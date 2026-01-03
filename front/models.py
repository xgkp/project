from django.db import models

# Create your models here.
class book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField(null=True)
    price = models.FloatField()

class bookoder(models.Model):
    book = models.ForeignKey(book, on_delete=models.CASCADE)
    sale_price = models.FloatField()
    
