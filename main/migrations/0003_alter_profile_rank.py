# Generated by Django 4.0 on 2022-01-18 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rank',
            field=models.IntegerField(),
        ),
    ]