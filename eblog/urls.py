from django.conf.urls import patterns, include, url
from . import views, feed

urlpatterns = patterns(
    '',
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url(r'^feed/$', feed.LatestPosts(), name="feed"),
    url(r'^post/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
    url(r'^about-me/$', views.AboutMe.as_view(), name='about-me'),
)
