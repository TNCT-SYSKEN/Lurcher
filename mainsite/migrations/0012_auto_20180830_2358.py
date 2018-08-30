# Generated by Django 2.1 on 2018-08-30 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0011_auto_20180830_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offlineparty',
            name='access_token',
        ),
        migrations.RemoveField(
            model_name='offlineparty',
            name='access_token_secret',
        ),
        migrations.AddField(
            model_name='account',
            name='access_token',
            field=models.CharField(default='', max_length=512, verbose_name='アクセストークン'),
        ),
        migrations.AddField(
            model_name='account',
            name='access_token_secret',
            field=models.CharField(default='', max_length=512, verbose_name='アクセストークンシークレット'),
        ),
    ]
