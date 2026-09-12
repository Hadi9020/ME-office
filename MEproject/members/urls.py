from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='members/index'),
        path('search/<str:target>/', views.search, name='members/search'),
        path('profile/<int:pk>/', views.profile, name='members/profile'),
]