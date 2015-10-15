'''
Created on May 13, 2014

@author: a141890
'''
from django.conf import settings
from django.db.models.base import Model
from django.db.models.fields import CharField, TextField, DateTimeField
from django.db.models.fields.related import ForeignKey
from datetime import datetime
import re
from django.contrib.auth import get_user_model


class IlbeArticleModel(Model):
    title = CharField(max_length=200)
    content = TextField()
    author = ForeignKey(get_user_model())
    
    registed = DateTimeField()
    class Meta:
        db_table = "ilbe_articles"
        
    def __unicode__(self):
        return unicode(self.title)
        
        

