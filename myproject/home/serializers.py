

from rest_framework import serializers
from .models import Blog
from rest_framework.authtoken.models import Token

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

        

