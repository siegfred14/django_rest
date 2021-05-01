from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

# Create your views here.


def home(request):
    data = {
        "message": "This is a json response"
    }

    return JsonResponse(data)
