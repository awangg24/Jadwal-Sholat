# Generated by Django 4.1.3 on 2022-12-22 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_surah_alter_jadwal_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nomor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Nomor',
            },
        ),
    ]