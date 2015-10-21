from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hbi_crawler.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.show_articles_view),
    url(r'^articles/$', views.show_articles_view),
)
