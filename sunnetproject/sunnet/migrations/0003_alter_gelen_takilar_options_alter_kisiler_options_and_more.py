# Generated by Django 4.1.7 on 2023-03-23 08:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sunnet', '0002_rename_kisi_id_gelen_takilar_kisi_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gelen_takilar',
            options={'verbose_name': 'Gelen Ganimet', 'verbose_name_plural': 'Gelen Ganimetler'},
        ),
        migrations.AlterModelOptions(
            name='kisiler',
            options={'verbose_name': 'Kime Gelen Ganimet', 'verbose_name_plural': 'Kime Gelen Ganimetler'},
        ),
        migrations.AlterModelOptions(
            name='taki_turu',
            options={'verbose_name': 'Ganimet Türü', 'verbose_name_plural': 'Ganimet Türleri'},
        ),
        migrations.AddField(
            model_name='gelen_takilar',
            name='ekleme_tarihi',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gelen_takilar',
            name='guncelleme_tarihi',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
