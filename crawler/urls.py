from django.conf.urls import url

from crawler import views

app_name = 'crawler'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^$', views.IndexView.as_view(), name='index'),
]