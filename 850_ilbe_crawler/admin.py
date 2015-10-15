from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from models import IlbeArticleModel

# Register your models here.


class IlbeArticleAdmin(ModelAdmin):
    class Meta: 
        model = IlbeArticleModel
        
admin.site.register(IlbeArticleModel, IlbeArticleAdmin)