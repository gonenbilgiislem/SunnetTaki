# Generated by Django 4.1.7 on 2023-03-25 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunnet', '0008_alter_gelen_takilar_guncelleme_tarihi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gelen_takilar',
            name='MIKTAR',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
    ]