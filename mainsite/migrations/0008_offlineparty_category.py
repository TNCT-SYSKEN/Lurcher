# Generated by Django 2.1 on 2018-08-28 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0007_auto_20180828_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='offlineparty',
            name='category',
            field=models.ManyToManyField(to='mainsite.Category'),
        ),
    ]