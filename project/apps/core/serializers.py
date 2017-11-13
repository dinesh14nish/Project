from rest_framework import serializers
from .models import University, Student

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'  # all model fields will be included

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'  # all model fields will be included