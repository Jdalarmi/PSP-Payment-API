from django.urls import path
from .import views
urlpatterns = [
    path('register_user/', views.login, name='register_user'),
    path('listar/', views.listar, name='listar')
]
