# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Cars(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_make = models.TextField()
    car_model = models.TextField()
    car_year = models.IntegerField()
    car_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cars'
        app_label = 'topsales'

class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_phone = models.TextField()

    class Meta:
        managed = False
        db_table = 'customers'
        app_label = 'topsales'


class Sales(models.Model):
    sale_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)
    car = models.ForeignKey(Cars, models.DO_NOTHING, blank=True, null=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sale_rep = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales'
        app_label = 'topsales'
