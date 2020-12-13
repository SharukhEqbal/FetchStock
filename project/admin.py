from django.contrib import admin
from project.models import Stock, Price, DateRecord

# Register your models here.

# Registered to use in admin page
# To access create an admin user
admin.site.register(Stock)
admin.site.register(Price)
admin.site.register(DateRecord)
