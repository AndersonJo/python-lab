'''
Created on May 14, 2014

@author: a141890
'''
from django.forms.models import ModelForm
from models import IlbeArticleModel
from datetime import datetime
import re

class IlbeArticleForm(ModelForm):
    
    class Meta:
        model = IlbeArticleModel
    
    def clear_title(self):
        title = self.cleaned_data['title']
        title = re.sub('\s+', ' ', title).strip()
        
        print 'clear_title :', title
        return title
        
    def clear_registed(self):
        return datetime.now()