from django.urls import path
from . import views
urlpatterns = [
    path('list/', views.bookList, name='bookList'),
    path('detail/', views.bookDetail, name='bookDetail')
]