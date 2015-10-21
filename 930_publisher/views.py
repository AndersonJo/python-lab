# -*- coding:utf-8 -*-

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from publisher.models import PublisherModel, BookModel

# Create your views here.

def test_view(request):
    # users
    mket, created = get_user_model().objects.get_or_create(username='MKET')
    if created:
        mket.email = "a141890@gmail.com"
        mket.set_password('1234')
        mket.save()
    
    # publishers
    mketPb, created = PublisherModel.objects.get_or_create(name=u'MKET Publisher', user=mket)
    oreilly, created = PublisherModel.objects.get_or_create(name=u'오레일리', user=mket)
    kb, created = PublisherModel.objects.get_or_create(name=u'교보문고', user=mket)
    
    # books
    book1, created = BookModel.objects.get_or_create(title=u'걸리버 여행기')
    if created:
        book1.publishers.add(mketPb)
        book1.publishers.add(oreilly)
        book1.save()
        
    poter, created = BookModel.objects.get_or_create(title=u'해리포터와 파이썬')
    if created:
        poter.publishers.add(mketPb)
        poter.publishers.add(kb)
        poter.save()
        
    hi, created = BookModel.objects.get_or_create(title=u'안녕 오드리햅번')
    if created:
        hi.publishers.add(mketPb)
        hi.save()
    
    
    # Tags
    
    
    
    
    
    
    