# Generated by Django 4.1.7 on 2023-03-25 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunnet', '0006_alter_gelen_takilar_taki_tur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gelen_takilar',
            name='ekleme_tarihi',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
