# Generated by Django 3.2.8 on 2021-12-22 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cash',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
