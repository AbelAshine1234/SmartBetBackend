from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

from users.models import UserCreated
from users.serializers import UserCreatedSerializer


class GetUser(APIView):
   
    def get(self,request,pk,format=None):
      try:
          user=UserCreated.objects.get(pk=pk)
          user_serialized=UserCreatedSerializer(user)
          return Response(user_serialized.data,status=status.HTTP_200_OK)
      except:
          return Response({"message":"could not found user"},status=status.HTTP_404_NOT_FOUND)
    




class UserCreatedView(APIView):
    def get(self,request,format=None):
        users=UserCreated.objects.all()
        users_serialized=UserCreatedSerializer(users,many=True)
        return Response(users_serialized.data)

    def post(self,request,format=None):
        serializer=UserCreatedSerializer(data=request.data)
        if serializer.is_valid():
            import re
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            match = re.match(pattern, request.data.get("email"))
            if match is None:
                return Response({"email":"is not valid"},status=status.HTTP_400_BAD_REQUEST)

            if(len(request.data.get('email'))<4):
                return Response({"email ":"is not valid"})
            if(len(request.data.get("password"))<8):
                return Response({"password length":"should be greater than 8"})
            
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class UserList(generics.ListCreateAPIView):
    queryset=UserCreated.objects.all()
    serializer_class=UserCreatedSerializer