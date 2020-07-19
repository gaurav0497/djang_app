from django.db import models
from datetime import datetime

# Create your models here.

class Product(models.Model):

    id = models.AutoField
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    date = models.DateField()
    image = models.ImageField(upload_to="shoopeasy/images", default="")

    def __str__(self):
        return self.name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=50)
    cust_email = models.CharField(max_length=80, default="")
    cust_phone = models.CharField(max_length=12, default="")
    cust_desc = models.CharField(max_length=400, default="")

    def __str__(self):
        return self.cust_name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    json_data = models.CharField(max_length=2000)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=500, default="")
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class UpdateOrder(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    time = models.DateField(default=datetime.now())

    def __str__(self):
        return self.update_desc[0:10]+"...."
