from django.conf.urls import url
from . import views


app_name = 'my_website'


urlpatterns = [
    url(r'^resume/$', views.resume, name='resume'),
    url(r'^work/$', views.work, name='work'),

]
