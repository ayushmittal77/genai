from django import forms
from .models import DocumentFile


class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = DocumentFile
        fields = ['file']