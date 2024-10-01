from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=70)
    roll_number = serializers.IntegerField()
    city = serializers.CharField(max_length=70)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll_number = validated_data.get('roll_number', instance.roll_number)
        instance.city = validated_data.get('city', instance.city)
        instance.save()

        return instance