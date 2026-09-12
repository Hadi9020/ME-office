from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='news/many'),
        path('search/<str:target>/', views.search, name='news/search'),
        path('news/<int:pk>/', views.news_detail, name='news/detail'),
]