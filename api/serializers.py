from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    reg_no = serializers.CharField()

    class Meta:
        model = Student
        fields = ('id', 'name', 'email', 'reg_no')
