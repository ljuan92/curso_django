from django.urls import path
from . import views
urlpatterns = [
    path('list/', views.bookList, name='bookList'),
    path('detail/<int:id>/', views.bookDetail, name='bookDetail')
]