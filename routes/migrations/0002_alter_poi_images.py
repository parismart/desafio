# Generated by Django 4.0.6 on 2022-07-21 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poi',
            name='images',
            field=models.CharField(default='None', max_length=800),
        ),
    ]