from django.urls import path, include
# from .views import home
from . import views

urlpatterns = [
    path('create-user/', views.UserCreate.as_view(), name='account-create')
]
