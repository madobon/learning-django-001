from django.db import models
import datetime

# Create your models here.
class Post(models.Model):
    '''
    投稿モデル
    '''
    keyword = models.CharField(max_length=30) # キーワード
    ip = models.CharField(max_length=20) # IP
    created_at = models.DateTimeField(auto_now_add=True) # 作成日時
    updated_at = models.DateTimeField(auto_now=True) # 更新日時

    def get_latest_keyword(self):
        obj = Post.objects.latest('id')
        return obj.keyword

    def get_previous_keyword(self):
        obj = Post.objects.filter(id=self.id-1)
        if obj:
            return obj.get(id=self.id-1).keyword
        return "Banana"

    keyword.short_descripton = 'キーワード'
    get_latest_keyword.short_descripton = '直前のキーワード'
    get_previous_keyword.short_descripton = '前回のキーワード'

    def __str__(self):
        return self.keyword