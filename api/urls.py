from django.urls import path, include
# from .views import home
from . import views

urlpatterns = [
    path('create-student/', views.StudentViews.as_view(), name="student")

]
