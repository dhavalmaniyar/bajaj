from rest_framework import serializers
from .dtos.response_dto import ResponseDto

class ResponseSerializer(serializers.ModelSerializer):
    is_success = serializers.BooleanField()
    user_id = serializers.CharField(max_length=200)
    odd = serializers.ListField(child=serializers.IntegerField())
    even = serializers.ListField(child=serializers.IntegerField())
    
    class Meta:
        model = ResponseDto
        fields = '__all__'