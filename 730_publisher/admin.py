from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from publisher.models import PublisherModel, BookModel, TagModel

# Register your models here.

class PublisherAdmin(ModelAdmin):
    class Meta:
        model = PublisherModel
        
class BookAdmin(ModelAdmin):
    class Meta:
        model = BookModel
        
class TagAdmin(ModelAdmin):
    class Meta:
        model = TagModel
        
admin.site.register(PublisherModel, PublisherAdmin)
admin.site.register(BookModel, BookAdmin)
admin.site.register(TagModel, TagAdmin)