from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer
from rest_framework.permissions import AllowAny

class RegisterUser(APIView):
    permission_class=[AllowAny]

    def post(self,request):
        serializer=RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_CREATED_201)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
