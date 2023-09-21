from rest_framework import serializers
from .models import Aiquest


class AiquestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aiquest
        fields = ['id', 'teacher_name', 'course_name', 'course_duration', 'seat']


# class AiquestSerializer(serializers.Serializer):
#     teacher_name = serializers.CharField(max_length=25)
#     course_name = serializers.CharField(max_length=25)
#     course_duration = serializers.IntegerField()
#     seat = serializers.IntegerField()

#     def create(self, validate_data):
#         return Aiquest.objects.create(**validate_data)
