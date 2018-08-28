# Generated by Django 2.1 on 2018-08-28 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0006_auto_20180827_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='offlineparty',
            name='participant',
            field=models.ManyToManyField(related_name='participant', to='mainsite.Account'),
        ),
        migrations.AlterField(
            model_name='offlineparty',
            name='sponsor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsor', to='mainsite.Account'),
        ),
    ]
