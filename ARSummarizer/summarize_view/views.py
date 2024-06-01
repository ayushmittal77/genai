import os
from django.shortcuts import render
from .forms import DocumentUploadForm
from summarize_app.summarizer.summarize import summarize_report

def summarize_document(request):
    summary = None
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()
            file_content = document.file.read()
            file_extension = os.path.splitext(document.file.name)[1][1:].lower()
            summary = summarize_report(file_content, file_extension)
    else:
        form = DocumentUploadForm()
    return render(request, 'upload_document.html', {'form': form, 'summary': summary})

