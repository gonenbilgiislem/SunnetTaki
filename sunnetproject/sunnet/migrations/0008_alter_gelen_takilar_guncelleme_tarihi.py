# Generated by Django 4.1.7 on 2023-03-25 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunnet', '0007_alter_gelen_takilar_ekleme_tarihi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gelen_takilar',
            name='guncelleme_tarihi',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]