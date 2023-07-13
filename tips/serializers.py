from rest_framework import serializers
from tips.models import TipsModel
class TipsSerializer(serializers.Serializer):
    id=serializers.CharField(required=False)
    title=serializers.CharField(required=True)
    content=serializers.CharField(required=True)
    class Meta:
        model=TipsModel
        fields="__all__"
    def create(self, validated_data):
        # return "d"
        return TipsModel.objects.create(**validated_data)