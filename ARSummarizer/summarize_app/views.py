from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from . import serializer
from .summarizer.summarize import summarize_report


class DocumentUploadAPIView(APIView):
    """
    API view to handle document uploads and summarization.

    This view accepts file uploads (PDF and DOCX formats) and returns a summarized 
    version of the content.
    """
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests for file uploads.

        This method handles the uploaded file, checks its format, and processes it 
        to generate a summary.

        Args:
            request (HttpRequest): The request object containing the uploaded file.

        Returns:
            Response: A DRF Response object containing the summary of the document 
            or an error message.
        """
        file_serializer = serializer.DocumentUploadSerializer(data=request.data)

        if file_serializer.is_valid():
            file = request.FILES['file']
            file_content = file.read()
            file_extension = file.name.split('.')[-1].lower()
            
            if file_extension in ['pdf', 'docx']:
                summary = summarize_report(file_content, file_extension)
                return Response({"summary": summary}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Unsupported file type"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
