# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

# from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.core.exceptions import ValidationError

class GELEN_TAKILAR(models.Model):
    # ID = models.AutoField(primary_key=True)
    AD = models.TextField(db_column='Ad')  # Field name made lowercase.
    SOYAD = models.TextField(db_column='Soyad', blank=True, null=True)  # Field name made lowercase.
    ACIKLAMA = models.TextField(blank=True, null=True)
    MIKTAR = models.DecimalField(max_digits=19,decimal_places=2,blank=True, null=True)
    TAKI_TUR = models.ForeignKey('TAKI_TURU', models.PROTECT, blank=True, null=True)
    KISI = models.ForeignKey('KISILER', models.PROTECT, blank=True, null=True)
    ekleme_tarihi = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True , blank=True, null=True)


    def clean(self):
        if (self.MIKTAR) < 0:
            raise ValidationError(
                {'MIKTAR': "Lütfen 0'dan büyük bir değer giriniz."})

    def __str__(self):
        return self.AD

    class Meta:
        verbose_name = "Gelen Ganimet"
        verbose_name_plural = "Gelen Ganimetler"


class KISILER(models.Model):
    class Meta:
        verbose_name = "Kime Gelen Ganimet"
        verbose_name_plural = "Kime Gelen Ganimetler"
    def __str__(self):
            return self.AD
    AD = models.TextField(blank=True, null=True)

class TAKI_TURU(models.Model):
    class Meta:
        verbose_name = "Ganimet Türü"
        verbose_name_plural = "Ganimet Türleri"
    def __str__(self):
            return self.AD
    AD = models.TextField(blank=True, null=True)
