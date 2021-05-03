# from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse
#
# # Create your views here.
#
#
# def home(request):
#     data = {
#         "message": "This is a json response"
#     }
#
#     return JsonResponse(data)

# The request is made up of two things
 # The Endpoint
 # The Methods
 # - POST Creating
 # - GET Read
 # - PUT/PATCH Updating
 # - DELETE Deleting

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer


# making a post request
class StudentViews(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data)

    # def perform_create(self, serializer):
    #     return super().perform_create(serializer)

# @api_view(['POST'])
# def create_student(request):
#     student = Student.objects.all()
#     serializer = StudentSerializer(data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


class GetStudentViews(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# create an endpoint to update
class UpdateStudentViews(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
