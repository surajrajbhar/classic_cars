# This is an auto-generated Django model module.
# You'll have to do the following  to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customers(models.Model):
    customernumber      = models.IntegerField(db_column='customerNumber', primary_key=True)  # Field name made lowercase.
    customername        = models.CharField(db_column='customerName', max_length=50)  # Field name made lowercase.
    contactlastname     = models.CharField(db_column='contactLastName', max_length=50)  # Field name made lowercase.
    contactfirstname    = models.CharField(db_column='contactFirstName', max_length=50)  # Field name made lowercase.
    phone               = models.CharField(max_length=50)
    addressline1        = models.CharField(db_column='addressLine1', max_length=50)  # Field name made lowercase.
    addressline2        = models.CharField(db_column='addressLine2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    city                = models.CharField(max_length=50)
    state               = models.CharField(max_length=50, blank=True, null=True)
    postalcode          = models.CharField(db_column='postalCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    country             = models.CharField(max_length=50)
    salesrepemployeenumber = models.ForeignKey('Employees', models.DO_NOTHING, db_column='salesRepEmployeeNumber', blank=True, null=True)  # Field name made lowercase.
    creditlimit         = models.FloatField(db_column='creditLimit', blank=True, null=True)  # Field name made lowercase.
    customerlocation    = models.TextField(db_column='customerLocation')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Customers'
    def __str__(self):
        return f'{str(self.customernumber)}_{self.customername}'


class Employees(models.Model):
    employeenumber  = models.IntegerField(db_column='employeeNumber', primary_key=True)  # Field name made lowercase.
    lastname        = models.CharField(db_column='lastName', max_length=50)  # Field name made lowercase.
    firstname       = models.CharField(db_column='firstName', max_length=50)  # Field name made lowercase.
    extension       = models.CharField(max_length=10)
    email           = models.CharField(max_length=100)
    reportsto       = models.ForeignKey('self', models.DO_NOTHING, db_column='reportsTo', blank=True, null=True)  # Field name made lowercase.
    jobtitle        = models.CharField(db_column='jobTitle', max_length=50)  # Field name made lowercase.
    officecode      = models.ForeignKey('Offices', models.DO_NOTHING, db_column='officeCode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Employees'


class Offices(models.Model):
    officecode = models.CharField(db_column='officeCode', primary_key=True, max_length=10)  # Field name made lowercase.
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    addressline1 = models.CharField(db_column='addressLine1', max_length=50)  # Field name made lowercase.
    addressline2 = models.CharField(db_column='addressLine2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50)
    postalcode = models.CharField(db_column='postalCode', max_length=15)  # Field name made lowercase.
    territory = models.CharField(max_length=10)
    officelocation = models.TextField(db_column='officeLocation')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Offices'


class Orderdetails(models.Model):
    ordernumber     = models.ForeignKey('Orders', on_delete = models.CASCADE, db_column='orderNumber')  # Field name made lowercase.
    productcode     = models.OneToOneField('Products', on_delete =  models.CASCADE, db_column='productCode', primary_key=True)  # Field name made lowercase.
    quantityordered = models.IntegerField(db_column='quantityOrdered')  # Field name made lowercase.
    priceeach       = models.FloatField(db_column='priceEach')  # Field name made lowercase.
    orderlinenumber = models.SmallIntegerField(db_column='orderLineNumber')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrderDetails'
        unique_together = (('productcode', 'ordernumber'),)


class Orders(models.Model):
    ordernumber = models.IntegerField(db_column='orderNumber', primary_key=True)  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='orderDate')  # Field name made lowercase.
    requireddate = models.DateTimeField(db_column='requiredDate')  # Field name made lowercase.
    shippeddate = models.DateTimeField(db_column='shippedDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=15)
    comments = models.TextField(blank=True, null=True)
    customernumber = models.ForeignKey(Customers, models.DO_NOTHING, db_column='customerNumber')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Orders'


class Payments(models.Model):
    checknumber = models.CharField(db_column='checkNumber', primary_key=True, max_length=50)  # Field name made lowercase.
    paymentdate = models.DateTimeField(db_column='paymentDate')  # Field name made lowercase.
    amount = models.FloatField()
    customernumber = models.ForeignKey(Customers, models.DO_NOTHING, db_column='customerNumber')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payments'


class Productlines(models.Model):
    productline = models.CharField(db_column='productLine', primary_key=True, max_length=50)  # Field name made lowercase.
    textdescription = models.CharField(db_column='textDescription', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    htmldescription = models.TextField(db_column='htmlDescription', blank=True, null=True)  # Field name made lowercase.
    image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ProductLines'


class Products(models.Model):
    productcode = models.CharField(db_column='productCode', primary_key=True, max_length=15)  # Field name made lowercase.
    productname = models.CharField(db_column='productName', max_length=70)  # Field name made lowercase.
    productscale = models.CharField(db_column='productScale', max_length=10)  # Field name made lowercase.
    productvendor = models.CharField(db_column='productVendor', max_length=50)  # Field name made lowercase.
    productdescription = models.TextField(db_column='productDescription')  # Field name made lowercase.
    quantityinstock = models.SmallIntegerField(db_column='quantityInStock')  # Field name made lowercase.
    buyprice = models.FloatField(db_column='buyPrice')  # Field name made lowercase.
    msrp = models.FloatField(db_column='MSRP')  # Field name made lowercase.
    productline = models.ForeignKey(Productlines, models.DO_NOTHING, db_column='productLine', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Products'
