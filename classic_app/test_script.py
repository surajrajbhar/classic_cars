User.objects.bulk_create(user_list)


for c in ct:
    print(f'{c.customername} : {c.contactfirstname} : {c.contactlastname}') 

user_list = [User(username=f"{c.contactfirstname}_{c.contactlastname}",email='surajrajbhar94@gmail.com',password=make_password('Bizact123'),is_active=True,) for c in ct ]


User.objects.bulk_create(user_list) 