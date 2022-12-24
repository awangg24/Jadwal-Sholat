# Generated by Django 4.1.3 on 2022-12-22 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_rename_kota_tanggal_alter_tanggal_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Surah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomor', models.CharField(blank=True, max_length=100, null=True)),
                ('nama', models.CharField(blank=True, max_length=100, null=True)),
                ('nama_latin', models.CharField(blank=True, max_length=100, null=True)),
                ('jumlah_ayat', models.CharField(blank=True, max_length=100, null=True)),
                ('tempat_turun', models.CharField(blank=True, max_length=100, null=True)),
                ('arti', models.CharField(blank=True, max_length=100, null=True)),
                ('deskripsi', models.CharField(blank=True, max_length=100, null=True)),
                ('audio', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Surah',
            },
        ),
        migrations.AlterModelOptions(
            name='jadwal',
            options={'verbose_name_plural': 'Jadwal'},
        ),
    ]