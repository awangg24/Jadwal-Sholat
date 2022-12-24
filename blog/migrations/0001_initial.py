# Generated by Django 4.1.3 on 2022-11-28 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Jadwal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imsyak', models.CharField(blank=True, max_length=100, null=True)),
                ('shubuh', models.CharField(max_length=100)),
                ('terbit', models.CharField(max_length=100)),
                ('dhuha', models.CharField(max_length=100)),
                ('dzuhur', models.CharField(max_length=100)),
                ('ashr', models.CharField(max_length=100)),
                ('maghrib', models.CharField(max_length=100)),
                ('isya', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('kotam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.kota')),
            ],
        ),
    ]
