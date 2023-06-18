from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from tips.models import TipsModel
from tips.serializers import TipsSerializer
from rest_framework import status

# Create your views here.


class GetTipsView(APIView):
    def get(self,request,pk,format='json'):
        try:
            tips=TipsModel.objects.get(pk=pk)
            tips_serialized=TipsSerializer(tips)
            return Response(tips_serialized.data,status=status.HTTP_200_OK)
        except:
            return Response({"message":"could not found tips"},status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,pk,format='json'):
        try:
            tips=TipsModel.objects.get(pk=pk).delete()
            return Response({"delted"},status=status.HTTP_200_OK)
        except:
            return Response({"message":"could not found tips"},status=status.HTTP_404_NOT_FOUND)
        
class TipsView(APIView):
    
    def post(self,request,format='json'):
        serializer=TipsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class TipsViewChangeTitle(APIView):
    def put(self,request,pk,format='json'):
        try:
            tips=TipsModel.objects.get(pk=pk)
        except:
            return Response({"message":"could not found tips"},status=status.HTTP_404_NOT_FOUND)
        tips=TipsModel.objects.filter(pk=pk).update(title=request.data.get("title"))
        tips_raw=TipsModel.objects.get(pk=pk)
        tips_serialized=TipsSerializer(tips_raw)
        return Response(tips_serialized.data,status=status.HTTP_201_CREATED)
class TipsViewChangeContent(APIView):
    def put(self,request,pk,format='json'):
        try:
            tips=TipsModel.objects.get(pk=pk)
        except:
            return Response({"message":"could not found tips"},status=status.HTTP_404_NOT_FOUND)
        tips=TipsModel.objects.filter(pk=pk).update(content=request.data.get("content"))
        tips_raw=TipsModel.objects.get(pk=pk)
        tips_serialized=TipsSerializer(tips_raw)
        return Response(tips_serialized.data,status=status.HTTP_201_CREATED)

