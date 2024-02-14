from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, viewsets
from .models import File
from .serializers import FileSerializer
# Create your views here.

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    
    def create(self, request, *args, **kwargs):
        print(request)
        return "POST"

    def destroy(self, request, *args, **kwargs):
        return "DEL"

    def retrieve(self, request, *args, **kwargs):
        print(request, 'is coming for GET')
        return "GET"
    
    def list(self, request, *args, **kwargs):
        return "GET LIST"