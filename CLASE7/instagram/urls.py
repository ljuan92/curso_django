from django.urls import path
from . import views

urlpatterns = [
    path('home/<int:user_id>/', views.Home, name='home')
]