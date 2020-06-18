from django.conf.urls import url
from django.contrib import admin
# from django.contrib.auth.views import login
from django.urls import path
from django.conf.urls import url, include
from . import views
app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_no>/', views.display_posts, name='display_posts'),
    path('comments/<int:post_no>/', views.display_comments, name='display_comments'),
    path('delete_post/<int:post_no>/', views.delete_post, name='delete_post'),
    path('write_comment/<int:post_no>/', views.write_comment, name='write_comment'),
    path('delete_comment/<int:comment_no>/', views.delete_comment, name='delete_comment'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^enter', views.enter, name='enter'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^my_blogs', views.my_blogs, name='my_blogs'),
    url(r'^write_post', views.write_post, name='write_post'),
]
