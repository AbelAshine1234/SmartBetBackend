from rest_framework import serializers
from analysis.models import AnalysisModel
class TipsSerializer(serializers.Serializer):
    title=serializers.CharField(required=True)
    content=serializers.CharField(required=True)
    class Meta:
        model=AnalysisModel
        fields="__all__"
    def create(self, validated_data):
        return AnalysisModel.objects.create(**validated_data)