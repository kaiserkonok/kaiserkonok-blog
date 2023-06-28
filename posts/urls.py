from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('search/', views.search, name='search'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
]
