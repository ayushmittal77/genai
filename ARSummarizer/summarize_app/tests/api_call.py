import argparse
import os
import requests

def upload_document(file_path, file_name):
    """
    Upload a document to the document upload API and print the summary.

    Args:
        file_path (str): The path to the document file to be uploaded.
        file_name (str): The name of the document file.

    Returns:
        None
    """
    try:
        # Open the document file in binary mode and read its content
        with open(file_path, 'rb') as f:
            file_content = f.read()
    except FileNotFoundError:
        print(f'Error: File not found at {file_path}')
        return
    except IOError:
        print(f'Error: Could not read file at {file_path}')
        return

    # Construct the request payload
    payload = {'file': (file_name, file_content)}
    
    # Send a POST request to the API endpoint
    response = requests.post('http://localhost:8000/api/upload-document/', files=payload)

    print("Response Code:", response.status_code)

    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        data = response.json()
        summary = data.get('summary')
        print(summary)
    else:
        print(f'Failed to upload document: HTTP {response.status_code}')

def main():
    """
    Parse command line arguments and upload the specified document.
    """
    parser = argparse.ArgumentParser(description='Upload a document to the document upload API and get a summary.')
    parser.add_argument('file_path', type=str, nargs='?', help='The path to the document file to be uploaded.')

    args = parser.parse_args()

    if not args.file_path:
        print('Error: No file path provided. Please provide the path to the document file to be uploaded.')
        return

    file_path = args.file_path
    file_name = os.path.basename(file_path)

    if not os.path.isfile(file_path):
        print(f'Error: Invalid file path. File does not exist at {file_path}')
        return

    upload_document(file_path, file_name)

if __name__ == '__main__':
    main()
