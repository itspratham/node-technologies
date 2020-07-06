from django.db import models

# Create your models here.
class UserLogin(models.Model):
    username = models.CharField(null=False,blank=False,max_length=200)
    password = models.CharField(null=False,blank=False,max_length=50)

    def __str__(self):
        return str(self.username)


type_choice = (("mobile","mobile"),("laptop","laptop"))

class Product(models.Model):
    name = models.TextField(null=False,blank=False,max_length=50)
    image = models.ImageField()
    description = models.TextField(null=False,blank=False,max_length=500)
    type = models.CharField(choices=type_choice,null=False,blank=False,max_length=50)

    def __str__(self):
        return str(self.name)

class MobileData(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True, blank=True)
    processor = models.CharField(max_length=100,null=True,blank=True)
    ram = models.IntegerField(null=True,blank=True)
    screen_size = models.CharField(max_length=20,null=True,blank=True)
    color = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return str(self.product.name)


class LaptopData(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True, blank=True)
    processor = models.CharField(max_length=100, null=True, blank=True)
    ram = models.IntegerField(null=True, blank=True)
    hard_drive_capacity = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.product.name)

