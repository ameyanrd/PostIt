from django.conf.urls import url
from django.contrib import admin
# from django.contrib.auth.views import login
from django.urls import path
from django.conf.urls import url, include
from . import views
app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^enter', views.enter, name='enter'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    # url(r'^account/$', views.index, name='account'),
    # url(r'^blogs/$', views.index, name='blogs'),

    # url(r'^$',views.index,name='index'),
    # url(r'^special/',views.special,name='special'),
    # path('blogs/', include('blogs.urls')),
    # url(r'^login/$', login, name='login'),
    # url(r'^logout/$', auth_views.logout, name='logout')
]