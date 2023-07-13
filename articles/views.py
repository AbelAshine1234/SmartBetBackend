from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from articles.models import ArticlesModel
from articles.serializers import ArticlesSerializer
from rest_framework import status

# Create your views here.


class GetArticlesView(APIView):
    def get(self,request,pk,format='json'):
        try:
            articles=ArticlesModel.objects.get(pk=pk)
            articles_serialized=ArticlesSerializer(articles)
            return Response(articles_serialized.data,status=status.HTTP_200_OK)
        except:
            return Response({"message":"could not found articles"},status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,pk,format='json'):
        try:
            articles=ArticlesModel.objects.get(pk=pk).delete()
            return Response({"delted"},status=status.HTTP_200_OK)
        except:
            return Response({"message":"could not found articles"},status=status.HTTP_404_NOT_FOUND)
        
class ArticlesView(APIView):
    def get(self,request,format='json'):
        art=ArticlesModel.objects.all()
        art_s=ArticlesSerializer(art,many=True)
        return Response(art_s.data)
    
    def post(self,request,format='json'):
        serializer=ArticlesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class ArticlesViewChangeTitle(APIView):
    def put(self,request,pk,format='json'):
        try:
            articles=ArticlesModel.objects.get(pk=pk)
        except:
            return Response({"message":"could not found articles"},status=status.HTTP_404_NOT_FOUND)
        articles=ArticlesModel.objects.filter(pk=pk).update(title=request.data.get("title"))
        articles_raw=ArticlesModel.objects.get(pk=pk)
        articles_serialized=ArticlesSerializer(articles_raw)
        return Response(articles_serialized.data,status=status.HTTP_201_CREATED)
class ArticlesViewChangeContent(APIView):
    def put(self,request,pk,format='json'):
        try:
            articles=ArticlesModel.objects.get(pk=pk)
        except:
            return Response({"message":"could not found articles"},status=status.HTTP_404_NOT_FOUND)
        articles=ArticlesModel.objects.filter(pk=pk).update(content=request.data.get("content"))
        articles_raw=ArticlesModel.objects.get(pk=pk)
        articles_serialized=ArticlesSerializer(articles_raw)
        return Response(articles_serialized.data,status=status.HTTP_201_CREATED)

