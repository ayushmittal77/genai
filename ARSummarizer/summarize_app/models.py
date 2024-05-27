from django.db import models

class Document(models.Model):
    """
    Model representing a document with an associated file and summary.
    
    Attributes:
        file (FileField): The file uploaded by the user.
        summary (TextField): A brief summary or description of the file.
        uploaded_at (DateTimeField): The date and time when the file was uploaded.
    """
    file = models.FileField(upload_to='uploaded_files/')
    summary = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns the name of the uploaded file.
        
        Returns:
            str: The name of the file.
        """
        return self.file.name
