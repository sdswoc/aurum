from django.contrib import admin
from django.conf.urls import include,url
from  posts  import views as abc


urlpatterns = [

url(r'^$'                         , abc.post_home   , name='list'      ) ,
url(r'^create/$'                  , abc.post_create                ) ,
url(r'^detail/(?P<id>\d+)/$'      , abc.post_detail , name='detail') ,
url(r'^update/(?P<id>\d+)/$'      , abc.post_update , name='update') ,
url(r'^delete/(?P<id>\d+)$'       , abc.post_delete , name='delete') ,


]