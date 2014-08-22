from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin
from django.contrib.admin.options import TabularInline
from lab_board.models import ArticleModel, ArticleImageModel

class ArticleImageAdmin(TabularInline):
    model = ArticleImageModel

class ArticleAdmin(ModelAdmin):
    inlines = [ArticleImageAdmin]
    class Meta:
        model = ArticleModel




admin.site.register(ArticleModel, ArticleAdmin)
