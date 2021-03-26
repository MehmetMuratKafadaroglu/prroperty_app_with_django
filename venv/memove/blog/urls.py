from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    #post views
    path('', views.PostListView.as_view(), name='post_list'),
    #path('', views.post_list, name='post_list'),
    path('property/<int:pk>-<slug:slug>/', views.post_detail, name='post_detail'),
    path('new/', views.PostCreateView.as_view(), name='post'),
]