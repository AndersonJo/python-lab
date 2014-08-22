from mket_paginator._paginator import MketPaginator
from lab_board.models import ArticleModel


__author__ = 'a141890'


def board_processor(request):
    page = int(request.GET.get('page', 1))

    query = {}

    articles = ArticleModel.objects.filter()
    paginator = MketPaginator(articles, current_page=page, per_page=5, page_range=5)
    articles = paginator.page(page)

    response = {}
    response['paginator'] = paginator
    return response