from django.db import models
from django.utils import timezone
# Create your models here.

#お知らせ記事のモデル
class article(models.Model):
  title = models.CharField('タイトル', max_length=255)
  text = models.TextField('本文')
  pub_date = models.DateTimeField('作成日', default=timezone.now)
