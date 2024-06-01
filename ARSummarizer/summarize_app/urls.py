"""
URL configuration for the document upload API.

This module defines the URL pattern for the document upload API view.
"""

from django.urls import path
from .views import DocumentUploadAPIView

urlpatterns = [
    path('upload-document/', DocumentUploadAPIView.as_view(), name='document_upload_api'),
]
