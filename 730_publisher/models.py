from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.conf import settings

# Create your models here.


class PublisherModel(Model):
    name = CharField(max_length=100)
    user = ForeignKey(settings.AUTH_USER_MODEL)
    
    class Meta:
        db_table = "publishers"
        
    def __unicode__(self):
        return unicode(self.name)
    
    
class BookModel(Model):
    title = CharField(max_length=100)
    publishers = ManyToManyField(PublisherModel, related_name='books')
    
    class Meta:
        db_table = 'books'
    
    def __unicode__(self):
        return unicode(self.title)
        

class TagModel(Model):
    name = CharField(max_length=50)
    book = ForeignKey(BookModel, related_name='tags')
    
    class Meta:
        db_table='book_tags'
    
    def __unicode__(self):
        return unicode(self.name)
        