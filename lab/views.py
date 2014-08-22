from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.generic.base import View
from lab_board.processors import board_processor

__author__ = 'a141890'


class BaseView(View):

    def get(self, request):

        processors = [board_processor]
        context = {}

        return render_to_response('lab/lab_board.html',
                                  context,
                                  context_instance=RequestContext(request, processors=processors))