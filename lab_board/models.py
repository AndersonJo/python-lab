# -*- coding:utf-8 -*-
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.db.models import ForeignKey
from django.db.models.fields import CharField, TextField, DateTimeField, IntegerField
from django.db.models.fields.files import ImageField


class ArticleModel(models.Model):

    key = CharField(max_length=100)
    user = ForeignKey(get_user_model())
    title = CharField(max_length=100)
    content = TextField()

    registered = DateTimeField()

    view_count = IntegerField(default=0)
    comment_count = IntegerField(default=0)

    class Meta:
        db_table = 'article'

    def __unicode__(self):
        return unicode(self.title)


class ArticleImageModel(models.Model):
    article = ForeignKey(ArticleModel, related_name='images')
    image = ImageField(upload_to='article_images/%Y/%m/%d')

    class Meta:
        db_table = 'article_image'
