from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from . import serializer


class DocumentUploadAPIView(APIView):
    
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):

        file_serializer = serializer.DocumentUploadSerializer(data=request.data)

        if file_serializer.is_valid():
            file = request.FILES['file']
            file_content = file.read()
            file_extension = file.name.split('.')[-1].lower()

        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
