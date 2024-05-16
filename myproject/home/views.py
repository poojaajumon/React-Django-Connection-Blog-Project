

from rest_framework import generics,status
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny 
from django.contrib.auth import authenticate  




class BlogListCreate(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticated,)  # Set the permission class

class BlogRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticated,)  


    def put(self, request, *args, **kwargs):
        instance = self.get_object()  # Get the instance to be updated
        serializer = self.get_serializer(instance, data=request.data)  # Initialize the serializer with instance and request data
        serializer.is_valid(raise_exception=True)  # Validate the serializer
        serializer.save()  # Save the updated instance
        return Response(serializer.data)





class LoginView(APIView):
    permission_classes = [AllowAny]  # Allow any user to access this view
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    def get(self, request):
        content = {
            "user": str(request.user),
            "auth": str(request.auth)
        }
        return Response(data=content, status=status.HTTP_200_OK)








