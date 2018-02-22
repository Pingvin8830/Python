from django.conf.urls import url
from page import views

urlpatterns = [
  url(r'^(?:(?P<cat_id>\d+)/)?$', views.index, name = "index"),
  url(r'^good/(?P<id>\d+)/$', views.good, name = "good"),
]

