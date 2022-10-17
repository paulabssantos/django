from turtle import ondrag
from unicodedata import name
from django.db import models

# Create your models here.

class State(models.Model):
    id = models.AutoField(db_column='id', primary_key=True, null=False)
    name = models.CharField(db_column='tx_name',null=False, blank=False, max_length=64)
    abbreviation = models.CharField(db_column='tx_abbreviation', null=False, max_length=2)

    class Meta:
        db_table = 'state'
        managed = True

class City(models.Model):
    id = models.AutoField(db_column='id', primary_key=True, null= False)
    name = models.CharField(db_column='tx_name',null=False, blank=False, max_length=64)
    state = models.ForeignKey(db_column='id_state',to='State', on_delete=models.DO_NOTHING, null=False, related_name='cities')

    class Meta:
        db_table = 'city'
        managed = True

class Disctrict(models.Model):
    id = models.AutoField(db_column='id', primary_key=True, null= False)
    name = models.CharField(db_column='tx_name',null=False, blank=False, max_length=64)
    city = models.ForeignKey(to='City',on_delete=models.DO_NOTHING,db_column='id_city',null=False)    
    zone = models.ForeignKey(to='Zone',on_delete=models.DO_NOTHING,db_column='id_zone',null=False)

    class Meta:
        db_table = 'district'
        managed = True

class Zone(models.Model):
    id = models.AutoField( primary_key=True)
    name = models.CharField(db_column='tx_name',null=False, max_length=64,unique=True)

    class Meta:
        db_table = 'zone'
        managed = True