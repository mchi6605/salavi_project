from django.urls import path
from . import views

app_name = 'sanpham'

urlpatterns = [
    path('', views.sanpham_list, name='list'),
    path('add/', views.sanpham_add, name='add'),
    path('<int:pk>/edit/', views.sanpham_edit, name='edit'),
    path('<int:pk>/delete/', views.sanpham_delete, name='delete'),
]
