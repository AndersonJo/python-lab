from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import views

# members/
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lab.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/$', views.LoginView.as_view()),

)
