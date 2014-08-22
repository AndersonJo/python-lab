from django.contrib.auth import authenticate, login
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from django.views.generic import View
from lab_member.forms import UserLoginForm


class LoginView(View):

    def get(self, request):

        processors = []
        context = {}
        context['login_form'] = UserLoginForm()
        return render_to_response('login/login.html',
                                  context,
                                  context_instance=RequestContext(request, processors=processors))

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['id']
            password = form.cleaned_data['password']

            user = authenticate(username=user_id, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')

        return HttpResponseRedirect(request.META['PATH_INFO'])