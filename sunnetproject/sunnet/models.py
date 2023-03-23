# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class GELEN_TAKILAR(models.Model):
    # ID = models.AutoField(primary_key=True)
    AD = models.TextField(db_column='Ad')  # Field name made lowercase.
    SOYAD = models.TextField(db_column='Soyad', blank=True, null=True)  # Field name made lowercase.
    ACIKLAMA = models.TextField(blank=True, null=True)
    MIKTAR = models.IntegerField(blank=True, null=True)
    TAKI_TUR_ID = models.ForeignKey('TAKI_TURU', models.SET_NULL, blank=True, null=True)
    KISI_ID = models.ForeignKey('KISILER', models.SET_NULL, blank=True, null=True)

class KISILER(models.Model):
    def __str__(self):
            return self.AD
    AD = models.TextField(blank=True, null=True)

class TAKI_TURU(models.Model):
    # ID = models.AutoField(primary_key=True)
    def __str__(self):
            return self.AD
    AD = models.TextField(blank=True, null=True)
