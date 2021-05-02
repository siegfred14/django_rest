from rest_framework import serializers
from .models import Student


class StudentSerializers(serializers.serializer):

    class Meta:
        model = Student
        fields = "__all__"
