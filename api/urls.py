from django.urls import path, include
# from .views import home
from . import views

urlpatterns = [
    # path('create-student/', views.create_student, name="student"),
    path('create-student/', views.StudentViews.as_view(), name="student"),
    path('get-student/', views.GetStudentViews.as_view(), name="get-student"),
    path('update-student/<int:pk>', views.UpdateStudentViews.as_view(), name="update-student")
]
