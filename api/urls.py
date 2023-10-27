from django.urls import path
from .import views
urlpatterns = [
    path('register_user/', views.login, name='register_user'),
    path('register_transaction/', views.register_transaction, name='register_transaction')
]
