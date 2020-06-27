from django.db import models

# Create your models here.
class UserLogin(models.Model):
    username = models.CharField(null=False,blank=False,max_length=200)
    password = models.CharField(null=False,blank=False,max_length=50)

    def __str__(self):
        return str(self.username)


type_choice = (("Mobile","Mobile"),("Laptop","Laptop"))

class Product(models.Model):
    name = models.TextField(null=False,blank=False,max_length=50)
    image = models.ImageField(null=True,blank=True)
    description = models.TextField(null=False,blank=False,max_length=500)
    type = models.CharField(choices=type_choice,null=False,blank=False,max_length=50)

    def __str__(self):
        return str(self.name)

class MobileData(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    processor = models.CharField(max_length=100,null=False,blank=False)
    ram = models.IntegerField(null=False,blank=False)
    screen_size = models.CharField(max_length=20,null=False,blank=False)
    color = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return str(self.product.name)


class LaptopData(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    processor = models.CharField(max_length=100, null=False, blank=False)
    ram = models.IntegerField(null=False, blank=False)
    hard_drive_capacity = models.IntegerField(null=False,blank=False)

    def __str__(self):
        return str(self.product.name)

