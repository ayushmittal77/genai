from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile

class DocumentUploadTests(APITestCase):
    """
    Test suite for the document upload API.
    """
    
    def setUp(self):
        """
        Set up the test suite with the URL of the document upload API.
        """
        self.url = reverse('document_upload_api') 

    def test_upload_valid_pdf(self):
        """
        Test uploading a valid PDF file.
        """
        with open('test_files/sample.pdf', 'rb') as pdf_file:
            response = self.client.post(self.url, {'file': pdf_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('summary', response.data)

    def test_upload_valid_docx(self):
        """
        Test uploading a valid DOCX file.
        """
        with open('test_files/sample.docx', 'rb') as docx_file:
            response = self.client.post(self.url, {'file': docx_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('summary', response.data)

    def test_upload_invalid_file_type(self):
        """
        Test uploading an invalid file type (TXT).
        """
        with open('test_files/sample.txt', 'rb') as txt_file:
            response = self.client.post(self.url, {'file': txt_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)

    def test_upload_no_file(self):
        """
        Test uploading with no file.
        """
        response = self.client.post(self.url, {}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('file', response.data)

    def test_upload_empty_file(self):
        """
        Test uploading an empty file.
        """
        empty_file = SimpleUploadedFile("empty.pdf", b"")
        response = self.client.post(self.url, {'file': empty_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('file', response.data)
