from .models import UserCreated
from rest_framework import serializers
from rest_framework.response import Response

class UserCreatedSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
            required=True,
            min_length=5,
            max_length=20
            ),
    email = serializers.CharField(
            required=True,
            min_length=5,
            max_length=20
            ),
    password = serializers.CharField(
            required=True,
            max_length=256
            )
    role = serializers.CharField(
            required=True,
            max_length=256
            )
   

    class Meta:
        model = UserCreated
        fields = ('username', 'password','role','email')

   
    def create(self, validated_data):
        user = UserCreated.objects.create_user(**validated_data)
        return user
    def update(self, instance, validated_data):
        return UserCreated.objects.update(instance, validated_data)
    
