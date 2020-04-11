

from .models import Customers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

ct =  Customers.objects.all()
ut = [User(username=c.customernumber,email='surajrajbhar94@gmail.com', password=make_password('Bizact123'),is_active=True,first_name=c.contactfirstname,last_name=c.contactlastname) 
for c in ct ]


usr_list = []

for c in ct:
    usr = User(username=c.customernumber,email='surajrajbhar94@gmail.com', password=make_password('Bizact123'),is_active=True,first_name=c.contactfirstname,last_name=c.contactlastname) 
    usr_list.append(usr)
