'''
Created on May 14, 2014

@author: a141890
'''
from models import IlbeArticleModel
from django.core.paginator import Paginator
def board_processor(request):
    response = {}
    page = int(request.GET.get('page', 1))
    
    rows = IlbeArticleModel.objects.all()
    paginator = Paginator(rows, 4)
    
    response['articles'] = paginator.page(page)
    return response