from rest_framework import serializers
from articles.models import ArticlesModel
class ArticlesSerializer(serializers.Serializer):
    title=serializers.CharField(required=True)
    content=serializers.CharField(required=True)
    class Meta:
        model=ArticlesModel
        fields="__all__"
    def create(self, validated_data):
        return ArticlesModel.objects.create(**validated_data)