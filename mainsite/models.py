from django.db import models
from .custom_fields import PositiveBigIntegerField

# Create your models here.

class Account(models.Model) :
    twitter_id = PositiveBigIntegerField('ツイッターID', blank = False)
    pref = models.CharField('都道府県', max_length = 255)
    evaluation = PositiveBigIntegerField('評価数', default = 0)
