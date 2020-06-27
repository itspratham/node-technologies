from django.contrib import admin

# Register your models here.
from .models import UserLogin,Product,LaptopData,MobileData

admin.site.register(UserLogin)
admin.site.register(Product)
admin.site.register(LaptopData)
admin.site.register(MobileData)