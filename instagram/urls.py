from django.urls import path,re_path
from . import views
app_name = 'instagram'
urlpatterns = [
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name="post_detail"),
    re_path(r'^(?P<username>[\w.@+-]+)/$', views.user_page, name='user_page'),
    path('post/<int:pk>/like', views.post_like, name="post_like"),
    path('post/<int:pk>/unlike', views.post_unlike, name="post_unlike"),
    path('post/<int:post_pk>/comment/new', views.comment_new, name="comment_new"),
    path('', views.index, name='index'),
]