from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .dtos.response_dto import ResponseDto
from .serializers import ResponseSerializer

# Create your views here.
class View(APIView):
    def post(self, request):
        even = [] 
        odd = [] 
        is_success = True
        tasks = request.data['numbers']
        for i in tasks:
            if not isinstance(i, int):
                is_success=False
                break
            elif i%2==0:
                even.append(i)
            elif i%2!=0:   
                odd.append(i)

        if not is_success:
            odd = []
            even = []
            
        response = ResponseDto(is_success, 1, odd, even)
        print(response.even)
        serializer = ResponseSerializer(response, many=False)
        return Response(serializer.data)
    