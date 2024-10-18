# Medical Examination Classification App

## Overview
This project is a web application built with Django and FastAPI that allows users to manage patient examinations, upload images, and classify them using a machine learning model. The application supports image classification between 'Melanoma' and 'Melanocytic Nevi' classes and provides a user-friendly interface for managing patient data and test records.

## Features
- User authentication system
- Upload and manage patient examinations
- Classify images using a trained PyTorch model
- View and manage patient information, including test records
- Responsive design for easy use on various devices

## Technologies Used
- Python
- Django
- FastAPI
- PyTorch
- HTML/CSS/JavaScript
- PostgreSQL (or any other database of your choice)

## Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- A virtual environment (recommended)

### Installation

1. Clone the repository:
```
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
```
2. Create and activate a virtual environment:
# Create a virtual environment
```
python -m venv venv
```
# Activate the virtual environment
# Windows
```
.\venv\Scripts\activate
```
# macOS/Linux
```
source venv/bin/activate
```
3. Install the required packages:
```
pip install -r requirements.txt
```
4. Apply database migrations:
```
python manage.py migrate
```
5. Create a superuser (optional):
```
python manage.py createsuperuser
```
6. Run the application:
```
python manage.py runserver
```
7. Access the application at
```
http://localhost:8000
```
## Usage

* Adding Examinations: Use the form to upload images and provide descriptions.
* Classifying Images: Select an image for classification to receive predictions and confidence levels.
* Managing Patients: View patient lists, add new patients, and manage their test records.
  
## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any changes or improvements but for the love of god dont ask me why I did it that way.

## License
This project is licensed under the MIT License

## Acknowledgements
* Django
* FastAPI
* PyTorch


















