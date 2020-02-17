from django.contrib import admin

# Register your models here.

from classic_app.models import *

admin.site.register(Payments)
admin.site.register(Customers)
admin.site.register(Employees)
admin.site.register(Offices)
admin.site.register(Orderdetails)
admin.site.register(Orders)
admin.site.register(Productlines)
admin.site.register(Products)