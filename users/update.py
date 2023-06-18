
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

from users.models import UserCreated
from users.serializers import UserCreatedSerializer

class ChangeRole(APIView):
    def put(self,request,pk,format=None):
        try:
            user = UserCreated.objects.get(pk=pk)
        except UserCreated.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        if(request.data.get("role") is None):
            return Response({"role":"is required"})
        user = UserCreated.objects.filter(pk=pk).update(role=request.data.get("role"))
        user_ras=UserCreated.objects.get(pk=pk)
        user_ser=UserCreatedSerializer(user_ras)
        return Response(user_ser.data,status=status.HTTP_200_OK)
        
class ChangeName(APIView):
    
    def put(self,request,pk,format=None):
        try:
            user = UserCreated.objects.get(pk=pk)
        except UserCreated.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        if(request.data.get("username") is None):
            return Response({"username":"is required"})
        user = UserCreated.objects.filter(pk=pk).update(username=request.data.get("username"))
        user_ras=UserCreated.objects.get(pk=pk)
        user_ser=UserCreatedSerializer(user_ras)
        return Response(user_ser.data,status=status.HTTP_200_OK)

        
class ChangePassword(APIView):
    
    def put(self,request,pk,format=None):
        try:
            user = UserCreated.objects.get(pk=pk)
        except UserCreated.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        if(request.data.get("password") is None):
            return Response({"password":"is required"})
        user = UserCreated.objects.filter(pk=pk).update(password=request.data.get("password"))
        user_ras=UserCreated.objects.get(pk=pk)
        user_ser=UserCreatedSerializer(user_ras)
        return Response(user_ser.data,status=status.HTTP_200_OK)

        
class ChangeEmail(APIView):
    
    def put(self,request,pk,format=None):
        try:
            user = UserCreated.objects.get(pk=pk)
        except UserCreated.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        if(request.data.get("email") is None):

            return Response({"email":"is required"})
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        match = re.match(pattern, request.data.get("email"))
        if match is None:
            return Response({"email":"is not valid"},status=status.HTTP_400_BAD_REQUEST)
        if(len(request.data.get('email'))<4):
            return Response({"email ":"is not valid"})
        user = UserCreated.objects.filter(pk=pk).update(email=request.data.get("email"))
        user_ras=UserCreated.objects.get(pk=pk)
        user_ser=UserCreatedSerializer(user_ras)
        return Response(user_ser.data,status=status.HTTP_200_OK)

