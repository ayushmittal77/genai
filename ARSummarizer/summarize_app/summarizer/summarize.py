from io import BytesIO
import PyPDF2
import docx


def read_document(file_content, file_extension):
    """
    Read the content of a document based on its file extension.
    
    Args:
        file_content (bytes): The content of the file.
        file_extension (str): The extension of the file ('pdf' or 'docx').

    Returns:
        str: The extracted text content of the document.
    """
    if file_extension == 'pdf':
        return read_pdf(file_content)
    elif file_extension == 'docx':
        return read_docx(file_content)
    else:
        raise ValueError("Unsupported file extension. Supported extensions are 'pdf' and 'docx'.")


def read_pdf(pdf_content):
    """
    Extract text from a PDF file.
    
    Args:
        pdf_content (bytes): The content of the PDF file.

    Returns:
        str: The extracted text content of the PDF.
    """
    pdf_text = ''
    pdf_reader = PyPDF2.PdfReader(BytesIO(pdf_content))
    for page_num in range(len(pdf_reader.pages)):
        pdf_text += pdf_reader.pages[page_num].extract_text()
    return pdf_text


def read_docx(docx_content):
    """
    Extract text from a DOCX file.
    
    Args:
        docx_content (bytes): The content of the DOCX file.

    Returns:
        str: The extracted text content of the DOCX.
    """
    docx_text = ''
    doc = docx.Document(BytesIO(docx_content))
    for paragraph in doc.paragraphs:
        docx_text += paragraph.text
    return docx_text


