from django.db import models
from .custom_fields import PositiveBigIntegerField

# Create your models here.

class Account(models.Model) :
    twitter_id = PositiveBigIntegerField('ツイッターID', blank = False)
    pref = models.CharField('都道府県', max_length = 255)
    evaluation = PositiveBigIntegerField('評価数', default = 0)
    held_count = PositiveBigIntegerField('開催数', default = 0)

    def __str__(self) :
        return str(self.twitter_id)

class Category(models.Model) :
    category = models.CharField('カテゴリ', max_length = 255)

    def __str__(self) :
        return str(self.category)

class AccountCategory(models.Model) :
    account = models.ForeignKey(Account, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self) :
        return str(self.account) + ': ' + str(self.category)

class OfflineParty(models.Model) :
    sponsor = models.ForeignKey(Account, on_delete = models.CASCADE, related_name='sponsor')
    title = models.CharField('タイトル', max_length = 255)
    at_time = models.DateTimeField('開催日時', null = True, blank=True)
    capacity = models.IntegerField('募集人数')
    participant = models.ManyToManyField(Account, related_name='participant')
    location_lat = models.FloatField('緯度', null = True, blank=True)
    location_lng = models.FloatField('経度', null = True, blank=True)
    recruitment_start = models.DateField('募集開始')
    recruitment_end = models.DateField('募集終了')
    comment = models.TextField('コメント')

    def __str__(self) :
        return self.title
