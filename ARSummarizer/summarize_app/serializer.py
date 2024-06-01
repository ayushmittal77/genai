from rest_framework import serializers


class DocumentUploadSerializer(serializers.Serializer):
    """
    Serializer for document upload.

    This serializer handles the validation of the file field in the upload request.
    """
    file = serializers.FileField()
