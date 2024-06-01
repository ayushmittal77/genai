from django.urls import path
from .views import summarize_document

urlpatterns = [
    path('', summarize_document, name='summarize_document'),
]