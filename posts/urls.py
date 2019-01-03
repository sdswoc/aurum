from django.contrib import admin
from django.conf.urls import include,url
from  posts  import views as abc


urlpatterns = [

url(r'^$'                              , abc.post_home   ,  name='list'    ) ,
url(r'^create/$'                       , abc.post_create ,  name='create'  ) ,
url(r'^detail/(?P<slug>[\w-]+)/$'      , abc.post_detail ,  name='detail'  ) ,
url(r'^update/(?P<slug>[\w-]+)/$'      , abc.post_update ,  name='update'  ) ,
url(r'^delete/(?P<slug>[\w-]+)$'       , abc.post_delete ,  name='delete'  ) ,
url(r'^comment/(?P<slug>[\w-]+)$'      , abc.post_comment , name='comment' ) ,

]
