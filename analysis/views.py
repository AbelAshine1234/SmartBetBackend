from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from analysis.models import AnalysisModel
from analysis.serializers import AnalysisSerializer
from rest_framework import status

# Create your views here.


class GetAnalysisView(APIView):
    def get(self,request,pk,format='json'):
        try:
            analysis=AnalysisModel.objects.get(pk=pk)
            analysis_serialized=AnalysisSerializer(analysis)
            return Response(analysis_serialized.data,status=status.HTTP_200_OK)
        except:
            return Response({"message":"could not found analysis"},status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,pk,format='json'):
        try:
            analysis=AnalysisModel.objects.get(pk=pk).delete()
            return Response({"delted"},status=status.HTTP_200_OK)
        except:
            return Response({"message":"could not found analysis"},status=status.HTTP_404_NOT_FOUND)
        
class AnalysisView(APIView):
    def get(self,request,format='json'):
        analysis=AnalysisModel.objects.all();
        analysis_serializer=AnalysisSerializer(analysis,many=True)
        return Response(analysis_serializer.data)
    
    def post(self,request,format='json'):
        serializer=AnalysisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class AnalysisViewChangeTitle(APIView):
    def put(self,request,pk,format='json'):
        try:
            analysis=AnalysisModel.objects.get(pk=pk)
        except:
            return Response({"message":"could not found analysis"},status=status.HTTP_404_NOT_FOUND)
        analysis=AnalysisModel.objects.filter(pk=pk).update(title=request.data.get("title"))
        analysis_raw=AnalysisModel.objects.get(pk=pk)
        analysis_serialized=AnalysisSerializer(analysis_raw)
        return Response(analysis_serialized.data,status=status.HTTP_201_CREATED)
class AnalysisViewChangeContent(APIView):
    def put(self,request,pk,format='json'):
        try:
            analysis=AnalysisModel.objects.get(pk=pk)
        except:
            return Response({"message":"could not found analysis"},status=status.HTTP_404_NOT_FOUND)
        analysis=AnalysisModel.objects.filter(pk=pk).update(content=request.data.get("content"))
        analysis_raw=AnalysisModel.objects.get(pk=pk)
        analysis_serialized=AnalysisSerializer(analysis_raw)
        return Response(analysis_serialized.data,status=status.HTTP_201_CREATED)

