# Generated by Django 4.1.3 on 2022-12-19 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_jadwal_maghrib_jadwal_magrib_jadwal_tanggal_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jadwal',
            options={'ordering': ['-tanggal'], 'verbose_name_plural': 'Jadwal'},
        ),
        migrations.RemoveField(
            model_name='jadwal',
            name='date',
        ),
        migrations.RemoveField(
            model_name='jadwal',
            name='kotam',
        ),
    ]