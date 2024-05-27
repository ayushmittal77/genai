# ARSummarizer

## Introduction
ARSummarizer is a Django-based application designed to summarize content. This README provides step-by-step instructions for setting up the project environment, cloning the repository, installing dependencies, and running the application.

## Prerequisites
Before you begin, ensure you have the following installed on your system:
- Anaconda/Miniconda
- Git
- Python 3.9

## Setup Instructions

### 1. Create and Activate a Conda Environment
First, create a new Conda environment with Python 3.9:
```bash
conda create --name <ENV_NAME> python=3.9
```

Activate the environment:
```bash
conda activate <ENV_NAME>
```

### 2. Clone the Repository
Navigate to the directory where you want to clone the repository:
```bash
cd /path/to/your/directory
```

Clone the repository from GitHub:
```bash
git clone <GITHUB_LINK>
```
Replace <GITHUB_LINK> with the URL of the GitHub repository.

### 3. Navigate to the Project Directory
Change to the project directory:
```bash
cd ARSummarizer/
```

### 4. Install Dependencies
Install the required packages:

```bash
pip install -r requirements.txt
```

### 5. Set Environment Variable
Create ```.env``` file in your root directory and add this to the file:

```bash
OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
```

### 5. Apply Migrations
Make migrations for the summarize_view app:

```bash
python manage.py makemigrations summarize_view
```
Apply the migrations to the database:

```bash
python manage.py migrate
```

### 6. Run the Development Server
Start the Django development server:

```bash
python manage.py runserver
```
The server will start, and you can access the application at http://127.0.0.1:8000/.

### 7. Run API Tests
To run the API call test, execute the following command, specifying the file path:
```bash
python summarize_app/tests/api_call.py <FILE_PATH>
```
Replace <FILE_PATH> with the path to the file you want to use for the API call.

## Contributing
If you wish to contribute to this project, please follow these steps:

- Fork the repository.
- Create a new branch for your feature or bugfix.
- Commit your changes to the new branch.
- Push your changes to your fork.
- Create a pull request to the main repository.

## License
This project is licensed under the Apache License. See the LICENSE file for more details.
