from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='coin/index'),
    path('<int:user_id>/', views.self, name='coin/self'),
]