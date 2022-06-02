from django.db import models
#ordermodel
import datetime

from django.db import models
from django.db.models import Sum, Count, Max
from django.template.defaultfilters import date
# Create your models here.

class Product(models.Model):
    product_image=models.ImageField(null=True)
    product_name = models.CharField(max_length=50)
    product_quantity = models.IntegerField()
    product_price = models.CharField(max_length=50)
    product_discription = models.CharField(max_length=100)
    def __str__(self):
        return self.product_name

class Employee(models.Model):
    firstname=models.CharField(max_length=50,null=True)
    lastname = models.CharField(max_length=50)
    sallary = models.IntegerField()
    mobnumber = models.IntegerField()
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.firstname

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name


#order model



class Order(models.Model):
    MONTHS = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct',
              11: 'Nov', 12: 'Dec'}

    product_name = models.CharField(max_length=40,null=True)
    price = models.IntegerField(null=True)
    product_quantity=models.IntegerField(null=True)
    created_time = models.DateTimeField(auto_now=True,null=True)
    updated_time = models.DateTimeField(auto_now=True,null=True)


    def __str__(self):
        return self.product_name