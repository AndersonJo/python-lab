from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from models import IlbeArticleModel
from processors import board_processor

# Create your views here.

def show_articles_view(request):
    context = {}
    processors = [board_processor]
    
    
    return render_to_response('crawler_board/articles.html', 
                              context,
                              context_instance=RequestContext(request, processors=processors))